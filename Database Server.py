#! /usr/bin/python3

from flask import Flask, render_template, request
import mysql.connector, json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def showSpeakers():
    with open('/home/l_taylor/CSCI240-Proposal/secret.json', 'r') as secretFile:
        creds = json.load(secretFile)['mysqlCredentials']
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    mycursor = connection.cursor()
    mycursor.execute("select * from Theater")
    myresult = mycursor.fetchall()

    mycursor.close()
    connection.close()
    return render_template('theater.html', collection=myresult)


if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")