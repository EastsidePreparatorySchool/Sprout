#imports flask
from flask import Flask
#Imports templates so we can use html
from flask import render_template
from flask import request
from markupsafe import escape
import main

app = Flask(__name__)

@app.route("/")
def test():
    return render_template('main.html')

@app.route("/slider/")
def slider():
    return "<p>Slideeeeeeeeeeeee!</p>"

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route('/user/<output>')
def show_user_profile(output):
    # show the user profile for that user
    return f'User {escape(output)}'

