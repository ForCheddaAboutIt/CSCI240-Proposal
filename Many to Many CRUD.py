from flask import Flask, render_template, request, redirect, url_for
import mysql.connector, os, json

with open('secret.json', 'r') as secretFile:
    creds = json.load(secretFile)['mysqlCredentials']

app = Flask(__name__)


@app.route('/actor', methods=['GET'])
def showActor():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    new_actor_id = request.args.get('new_actor_id')
    new_actor_name = request.args.get('new_actor_name')
    new_actor_birthdate = request.args.get('new_actor_birthdate')
    new_actor_height = request.args.get('new_actor_height')
    if new_actor_id is not None and new_actor_name is not None and new_actor_birthdate is not None and new_actor_height is not None:
        mycursor.execute("INSERT INTO Actor (Actor_ID, ActorName, BirthDate, Height_Inches) values (%s, %s, %s, %s)", (new_actor_id, new_actor_name, new_actor_birthdate, new_actor_height))
        connection.commit()

    # check to see if a student needs to be deleted
    delete_actor_id = request.args.get('delete_actor_id')
    if delete_actor_id is not None:
        try:
            mycursor.execute("delete from actor where id=%s",(delete_actor_id,))
            connection.commit()
        except:
            return render_template("error.html", message="Error deleting actor, perhaps they are in a movie")
        
    
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