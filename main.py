#imports flask sync test
from flask import Flask
#Imports templates so we can use html
from flask import render_template
from flask import request
from flask import redirect, url_for, session, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import escape
import os






db = SQLAlchemy()
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'Hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login_app.db'

users = {}
# class 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True)
    password = db.Column(db.String(25))

    def __init__(self, username):
        self.username = username
@login_manager.user_loader
def load_user(user_id):
    if user_id not in users:
        return
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = escape(request.form['username']) 
        password = escape(request.form['password'])
        user = User.query.filter_by(username=username).first()

        if username not in users or not check_password_hash(users[username], password):
             flash('Please check your login details and try again.')
             return redirect(url_for('login'))
        user = User(username)
        login_user(user)
        return redirect(url_for('protected'))
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists')
            return redirect(url_for('signup'))
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))

    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + str(current_user.id)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

@app.route("/")
def main():
    return redirect(url_for("login"))

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/test/")
def test():
    return render_template('test.html')

@app.route("/slider/0", methods=['GET', 'POST'])
def Slider0():
    return render_template('slider/slider0.html')

@app.route("/slider/1", methods=['GET', 'POST'])
def Slider1():
    return render_template('slider/slider1.html')

@app.route("/slider/2", methods=['GET', 'POST'])
def Slider_2():
    return render_template('slider/slider2.html')

@app.route("/slider/3", methods=['GET', 'POST'])
def Slider_3():
    return render_template('slider/slider3.html')

@app.route("/slider/4", methods=['GET', 'POST'])
def Slider_4():
    return render_template('slider/slider4.html')

@app.route("/slider/5", methods=['GET', 'POST'])
def Slider_5():
    return render_template('slider/slider5.html')

@app.route("/slider/6", methods=['GET', 'POST'])
def Slider_6():
    return render_template('slider/slider6.html')

@app.route("/slider/7", methods=['GET', 'POST'])
def Slider_7():
    return render_template('slider/slider7.html')

@app.route("/slider/8", methods=['GET', 'POST'])
def Slider_8():
    return render_template('slider/slider8.html')

@app.route("/slider/9", methods=['GET', 'POST'])
def Slider_9():
    return render_template('slider/slider9.html')

@app.route("/slider/10", methods=['GET', 'POST'])
def Slider_10():
    return render_template('slider/slider10.html')





