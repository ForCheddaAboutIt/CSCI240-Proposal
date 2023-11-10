import mysql.connector, json
from mysql.connector import Error 

with open('/home/l_taylor/CSCI240-Proposal/secret.json', 'r') as secretFile:
    creds = json.load(secretFile)['mysqlCredentials']


connection = mysql.connector.connect(**creds)

mycursor = connection.cursor()
mycursor.execute("select * from Theater")
myresult = mycursor.fetchone()

print("In the speaker table, we have the following items:")
while myresult is not None:
    print(myresult)
    myresult = mycursor.fetchone()

connection.close()
