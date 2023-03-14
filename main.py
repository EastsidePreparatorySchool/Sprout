from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<p>Sprout is Awesome!</p>"

@app.route("/slider")
def helle_world():
    return "<p>Slideeeeeeeeeeeee!</p>"
