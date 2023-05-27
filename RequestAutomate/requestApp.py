import requests
import mysql.connector
####
import httpx
import sys
import datetime
####
import inputFile
import time
####

print("Testing:")
import testing
print("")
print("Running the application:")
dbError = False
while True:
    try:
        conn = mysql.connector.connect(user='root', password='password',
                                host='mysql-container', database='nssf',port=3306)
        cursor = conn.cursor(buffered=True)
        cursor.execute("update sliceresource set available = 1")
        conn.commit()
    except mysql.connector.Error as err:
            # Handle database error
            dbError = True

    cursor.close()
    conn.close()
    for i in inputFile.input:
        dbError = False

        uid = i[0]
        app = i[1]
        headers = {'Content-Type': 'application/json'}
        print("Displaying for:")
        print("User ID:",uid)
        print("Desired Application:",app)
        try:
            conn = mysql.connector.connect(user='root', password='password',
                                    host='mysql-container', database='nssf',port=3306)
            cursor = conn.cursor(buffered=True)
                
            stmt = "select * from slicerepo where app = %(app)s"
            cursor.execute(stmt, {'app': app})
            res = cursor.fetchone()
            if res is None:
                print("Requested application not supported")
                # sys.exit()
                continue
            requestedNSSAI = res[0]
            print("User has requested for: " + str(requestedNSSAI))

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
            # sys.exit()
            continue

        
        with httpx.Client() as client:
            response = client.get('http://uploader:5000/app/api/amf', headers=headers, params={
                "uid": uid,
                "nssai": requestedNSSAI,
                "bwLower": res[6],
                "bwUpper": res[7],
                "latLower": res[8],
                "latUpper": res[9],
                "jitter": res[10]
            })

            print(response.status_code, end=" ")
            print(response.json())
            code = response.status_code
            if code == 400 or code == 403:
                # sys.exit()
                continue
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
            time.sleep(6)
            print("")
            
    