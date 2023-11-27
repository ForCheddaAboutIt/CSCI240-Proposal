from flask import Flask, render_template, request, redirect, url_for
import mysql.connector, os, json

with open('secret.json', 'r') as secretFile:
    creds = json.load(secretFile)['mysqlCredentials']

app = Flask(__name__)

@app.route('/', methods=['GET'])
def showHome():
    return render_template('base.html')

@app.route('/theater', methods=['GET'])
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

@app.route('/showing', methods=['GET'])
def showShowings():
    with open('/home/l_taylor/CSCI240-Proposal/secret.json', 'r') as secretFile:
        creds = json.load(secretFile)['mysqlCredentials']
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    newTheater_ID = request.args.get('theater_ID')
    newRoom = request.args.get('room')
    newDate = request.args.get('date')
    newSeats = request.args.get('seats')
    newMovie_ID = request.args.get('movie_ID')
    if newTheater_ID is not None and newRoom is not None and newDate is not None and newSeats is not None and newMovie_ID is not None:
        mycursor.execute("INSERT into Showing (Theater_ID, TheaterRoom, ShowingDate_Time, NumberSeats, Movie_ID) values (%s, %s, %s, %s, %s)", (newTheater_ID, newRoom, newDate, newSeats, newMovie_ID))
        connection.commit()
    # ...
    elif request.args.get('delete') == 'true':
        deleteID = request.args.get('id')
        deleteRoom = request.args.get('room')
        deleteDate = request.args.get('date')
        deleteSeats = request.args.get('seats')
        deleteMovie_ID = request.args.get('movie_ID')
        mycursor.execute("DELETE from Showing where Theater_ID=%s and TheaterRoom=%s and ShowingDate_Time=%s and NumberSeats=%s and Movie_ID=%s", (deleteID, deleteRoom, deleteDate, deleteSeats, deleteMovie_ID))
        connection.commit()
# ...

    

    mycursor.execute("select * from Showing")
    myresult = mycursor.fetchall()

    mycursor.close()
    connection.close()
    return render_template('showing.html', collection=myresult)

@app.route('/updateShowing')
def updateShowing():
    with open('/home/l_taylor/CSCI240-Proposal/secret.json', 'r') as secretFile:
        creds = json.load(secretFile)['mysqlCredentials']
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    newRoom = request.args.get('room')
    newDate = request.args.get('date')
    newSeats = request.args.get('seats')
    id = request.args.get('id')
    print("h")
    if id is None:
        return "Error, id not specified"
    elif newRoom is not None and newDate is not None and newSeats is not None:
        mycursor = connection.cursor()
        mycursor.execute("UPDATE Showing set TheaterRoom=%s, ShowingDate_Time=%s, NumberSeats=%s where Theater_ID=%s and TheaterRoom=%s and ShowingDate_Time=%s and NumberSeats=%s" (newRoom, newDate, newSeats, id, newRoom, newDate, newSeats))
        mycursor.close()
        connection.commit()
        connection.close()
        return redirect(url_for('showShowings'))

    mycursor = connection.cursor()
    mycursor.execute("select * from Showing where Theater_ID=%s;", (id,))
    _, existingName, existingHour, existingLocation = mycursor.fetchone()
    mycursor.close()
    connection.close()
    return render_template('theater-update.html', id=id, existingName=existingName, existingHour=existingHour, existingLocation=existingLocation)


@app.route('/actor', methods=['GET'])
def showActor():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    # If there is a section_id 'GET' variable, use this to refine the query
    movieID = request.args.get('movie_id')
    if movieID is not None:
        mycursor.execute("""SELECT Actor.Actor_ID, ActorName, BirthDate, Height_Inches, MoveTitle from Actor 
                         join Movie_Actor on Actor.Actor_ID=Movie_Actor.Actor_ID
                         join Movie on Movie.Movie_ID=Movie_Actor.Movie_ID
                         where Movie.Movie_ID=%s""", (movieID,))
        myresult = mycursor.fetchall()
        if len(myresult) >= 1:
            movieName = myresult[0][4]
        else:
            movieName = "Unknown"
        pageTitle = f"Showing all actors in movie: {movieName}"
    else:
        mycursor.execute("SELECT Actor_ID,ActorName,BirthDate,Height_Inches from Actor")
        pageTitle = "Showing all actors"
        myresult = mycursor.fetchall()

    mycursor.close()
    connection.close()
    return render_template('actor.html', actorList=myresult, pageTitle=pageTitle)


@app.route('/movie', methods=['GET'])
def showMovies():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    # If there is a student_id 'GET' variable, use this to refine the query
    actorID = request.args.get('actor_id')
    if actorID is not None:
        mycursor.execute("""SELECT Movie.Movie_ID, MoveTitle, Genre, Runtime, ReleaseDate, Rating, ActorName from Actor
                         join Movie_Actor on Actor.Actor_ID=Movie_Actor.Actor_ID
                         join Movie on Movie.Movie_ID=Movie_Actor.Movie_ID
                         where Actor.Actor_ID=%s""", (actorID,))
        myresult = mycursor.fetchall()
        print(myresult)

        if len(myresult) >= 1:
            actorName = myresult[0][6]
        else:
            actorName = "Unknown"
        pageTitle = f"Showing all movies for actor: {actorName}"

    else:
        mycursor.execute("""SELECT Movie_ID, MoveTitle, Genre, Runtime, ReleaseDate, Rating from Movie""")
        pageTitle = "Showing all movies"
        myresult = mycursor.fetchall()

    mycursor.close()
    connection.close()
    return render_template('movie.html', movieList=myresult, pageTitle=pageTitle)




if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")