#! /usr/bin/python3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def renderFormGet():
    output = render_template('form-get.html')
    return output 

@app.route('/submitformGet.html', methods=['GET'])
def renderTableGet():
    movietitle = request.args.get('mtitle')
    print(movietitle)
    genre = request.args.get('genre')
    rating = request.args.get('rating')
    output = render_template('table.html', mtitle=movietitle, genre=genre, rating=rating)
    return output 


if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")