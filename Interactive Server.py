#! /usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def showTheaters():
    with open('/home/l_taylor/CSCI240-Proposal/secret.json', 'r') as secretFile:
        creds = json.load(secretFile)['mysqlCredentials']
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    newName = request.args.get('name')
    newHour = request.args.get('hour')
    newLocation = request.args.get('location')
    if newName is not None and newHour is not None and newLocation is not None:
        mycursor.execute("INSERT into Theater (TheaterName, OperatingHours, Location) values (%s, %s, %s)", (newName, newHour, newLocation))
        connection.commit()
    elif request.args.get('delete') == 'true':
        deleteID = request.args.get('id')
        mycursor.execute("DELETE from Theater where Theater_ID=%s", (deleteID,))
        connection.commit()

    mycursor.execute("select * from Theater")
    myresult = mycursor.fetchall()

    mycursor.close()
    connection.close()
    return render_template('theater.html', collection=myresult)


@app.route('/updateTheater')
def updateTheaters():
    with open('/home/l_taylor/CSCI240-Proposal/secret.json', 'r') as secretFile:
        creds = json.load(secretFile)['mysqlCredentials']
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    newName = request.args.get('name')
    newHour = request.args.get('hour')
    newLocation = request.args.get('location')
    id = request.args.get('id')
    print("h")
    if id is None:
        return "Error, id not specified"
    elif newName is not None and newHour is not None and newLocation is not None:
        mycursor = connection.cursor()
        mycursor.execute("UPDATE Theater set TheaterName=%s, OperatingHours=%s, Location=%s where Theater_ID=%s", (newName, newHour, newLocation, id))
        mycursor.close()
        connection.commit()
        connection.close()
        return redirect(url_for('showTheaters'))

    mycursor = connection.cursor()
    mycursor.execute("select * from Theater where Theater_ID=%s;", (id,))
    _, existingName, existingHour, existingLocation = mycursor.fetchone()
    mycursor.close()
    connection.close()
    return render_template('theater-update.html', id=id, existingName=existingName, existingHour=existingHour, existingLocation=existingLocation)


if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")