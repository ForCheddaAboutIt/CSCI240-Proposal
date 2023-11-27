from flask import Flask, render_template, request, redirect, url_for
import mysql.connector, os, json

with open('secret.json', 'r') as secretFile:
    creds = json.load(secretFile)['mysqlCredentials']

app = Flask(__name__)


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