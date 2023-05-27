from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
import MySQLdb
import httpx
import datetime
##
# import testing
##

app = Flask(__name__)
app.secret_key = " "
app.config["MYSQL_HOST"] = "mysql-container" # host.docker.internal
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "nssf"
app.config["MYSQL_PORT"] = 3306

db = MySQL(app)

## change2
dbError = False;
# connecting to the database
try:
    conn = mysql.connector.connect(user='root', password='password',
                                   host='mysql-container', database='nssf',port=3306) #,port=3306
    cursor = conn.cursor()
except mysql.connector.Error as err:
    # Handle database error
    dbError = True
    error_message = str(err)
    error_message = "Database error:" + error_message
    # Send your own error code using httpx
    with httpx.Client() as client:
        response = client.post('http://127.0.0.1:5000/app/api/error', json={'error': error_message}) #   172.19.0.1   127.0.0.1
        print(response.status_code)
        print(response.json())
        print("Try again later")
    raise
## change2 -->

@app.route('/')
def index():
    return "NSSF"


@app.route('/app/api/amf', methods=['GET'])
def show():
    result = []
    if 'nssai' in request.args:
        requestedNSSAI = int(request.args['nssai'])
    else:
        return jsonify({'error': 'Bad Request'}), 400

    uid = int(request.args['uid'])

    # Authentication
    authPassed = True
    stmt = "select subs_NSSAI from subscriptions where userID= %(uid)s"
    cursor.execute(stmt, {'uid': uid})
    res = cursor.fetchall()
    allowedNSSAIS = []
    for i in res:
        allowedNSSAIS.append(i[0])
    print(requestedNSSAI)
    print(allowedNSSAIS)

    if requestedNSSAI not in allowedNSSAIS:
        authPassed = False

    if authPassed:
        print("User Authentication successful, request being redirected..")
    else:
        return jsonify({'error': 'Forbidden: SNSSAI_NOT_SUPPORTED'}), 403

    # forwarding request to nssf
    payload = {
        'uid': uid,
        'nssai': requestedNSSAI,
        'bwLower': float(request.args['bwLower']),
        'bwUpper': float(request.args['bwUpper']),
        'latLower': float(request.args['latLower']),
        'latUpper': float(request.args['latUpper']),
        'jitter': request.args['jitter']
    }
    return jsonify(payload), 200


@app.route('/app/api/nssf', methods=['POST'])
def selectSlice():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'No JSON data provided'}), 400
    print("Received this data:")
    print(data)

    params = {'uid', 'nssai', 'bwLower', 'bwUpper', 'latLower', 'latUpper', 'jitter'}
    if params.issubset(data.keys()):
        try:
            
            conn = mysql.connector.connect(user='root', password='password',
                                        host='mysql-container', database='nssf',port=3306) #host.docker.internal ,port=3306

            c = conn.cursor(buffered=True)
            # ##
            # try:
            #     query = "SELECT * FROM Network"
            #     c.execute(query)
            #     amf = c.fetchall()
            #     if len(amf)==0:
            #         return jsonify({'error': 'Slice not being serviced by any AMF'}), 404
            #     targetAMFSet=[row[0] for row in amf]
            #     return jsonify(targetAMFSet), 200
            # except:
            #     return jsonify({'error': 'Internal Server Error'}), 500
            # ###

            
            # query = f"SELECT * FROM sliceresource WHERE NSSAI='{data['nssai']}' AND available=1" # available=1
            # c.execute(query)
            query = "select snssai,sliceID from sliceresource where (bandWidth between %(bwlower)s and %(bwupper)s ) and (" \
                    "latency between %(latLower)s and %(latUpper)s ) and jitter=%(jitter)s and available=1 and " \
                    "nssai=%(nssai)s "
            
            c.execute(query, {'bwlower': data['bwLower'], 'bwupper': data['bwUpper'], 'latLower': data['latLower'],
                              'latUpper': data['latUpper'], 'jitter': data['jitter'], 'nssai': data['nssai']})
            

            slice = c.fetchone()
            
            # if slice!=None:
            if slice is not None:
                selected = slice[0]
                sliceID = slice[1]
                print(selected)
                c.execute("update sliceresource set available=0 where SNSSAI=%(selected)s", {'selected': selected})
                conn.commit()
                c.execute(f"SELECT * FROM amftable WHERE SliceId='{sliceID}'")
                amf = c.fetchall()
                result = []
                for row in amf:
                    result.append(row[0])
                if 'AMF-1' in result:
                    return jsonify({"SliceID": slice[0], "Serviced by default AMF": "AMF-1"}), 200
                response = {"SliceID": slice[0], "TargetAMF": result}
                
                return jsonify(response), 200
            else:
                return jsonify({'error': 'Slice not available at this moment'}), 404
        except mysql.connector.Error as err:
            print(err)
            return jsonify({'error': 'Internal Server Error'}), 500
    else:
        return jsonify({'error': 'Bad Request'}), 400
    

@app.route('/app/api/error', methods=['POST'])
def handle_error():
    error_data = request.json
    print(error_data['error'])
    if "Database error" in error_data['error']:
        return jsonify({'code': 500})

if __name__ == "__main__":
    app.run(debug=True)
