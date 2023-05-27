import requests
import mysql.connector
####
import httpx
import sys
import datetime
####
# import testing
####

print("Testing:")
import testing
print("")
print("Running the Application:")
dbError = False
uid = int(input("Enter your user id:"))
app = (input("Enter the desired application:")).strip()
headers = {'Content-Type': 'application/json'}

try:
    conn = mysql.connector.connect(user='root', password='password',
                               host='mysql-container', database='nssf',port=3306)
    cursor = conn.cursor(buffered=True)
        
    stmt = "select * from slicerepo where app = %(app)s"
    cursor.execute(stmt, {'app': app})
    res = cursor.fetchone()
    if res is None:
        print("Requested application not supported")
        sys.exit()
    requestedNSSAI = res[0]
    print("User has requested for: " + str(requestedNSSAI))

# cursor.close()
# conn.close()
except mysql.connector.Error as err:
    # Handle database error
    dbError = True
    error_message = str(err)
    error_message = "Database error:" + error_message
    # Send your own error code using httpx
    with httpx.Client() as client:
        response = client.post('http://uploader:5000/app/api/amf', json={'error': error_message})

        print(response.status_code)
        # print(response.content)
        print(response.json())

if dbError:
    print("Try again later")
    sys.exit()


with httpx.Client() as client:
    response = client.get('http://uploader:5000/app/api/amf', headers=headers, params={
        "uid": uid,
        "nssai": requestedNSSAI,
        "bwLower": float(res[6]),
        "bwUpper": float(res[7]),
        "latLower": float(res[8]),
        "latUpper": float(res[9]),
        "jitter": res[10]
    })
    # code = response.status_code
    # if code == 400:
    #     print("Incorrect http request")
    #     sys.exit()
    # elif code == 403:
    #     print("You are not authorized to access the requested resource. Please subscribe")
    #     sys.exit()
    # print(response.status_code)
    # print(response.json())
    # # testing.test_network_slice_selection()
    # headers = {'Content-Type': 'application/json'}
    print(response.status_code, end=" ")
    print(response.json())
    code = response.status_code
    if code == 400 or code == 403:
        sys.exit()
    ##
    def insert_record(datetime) :    
        try:
            cursor.execute("""
                INSERT INTO Network (datetime, value) VALUES
                (%s, %s)""", (datetime, uid))
            conn.commit()
        except mysql.connector.Error as e:
            print ("Error %d: %s" % (e.args[0], e.args[1]))
            conn.rollback()

    def update():
        insert_record(datetime.datetime.now()) # datetime according to system
        
    update()
    
    conn.commit()
    cursor.close()
    conn.close()
    ##
    response2 = client.post('http://uploader:5000/app/api/nssf', headers=headers, json=response.json())
    print(response2.json())


