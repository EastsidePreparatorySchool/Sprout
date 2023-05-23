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







app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'Hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
db = SQLAlchemy(app)

# class 
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True)
    password = db.Column(db.String(25))

    def __init__(self, username, password):
        self.username = username
        self.password = password

with app.app_context():    
    db.create_all()
    
@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return None  # Return None if user_id is None

    try:
        return User.query.get(int(user_id))
    except ValueError:
        return None  # Return None if user_id is not a valid integer


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = escape(request.form['username']) 
        password = escape(request.form['password'])
        user = User.query.filter_by(username=username).first()

        user = User(username, password)
        login_user(user)
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

       
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

# @app.route('/protected')
# @login_required
# def protected():
#     return 'Logged in as: ' + str(current_user.id)


# Navigation between Login and Signup

@app.route('/signupui')
def signupui():
    return render_template('signupui.html')

@app.route('/logininui')
def logininui():
    return render_template('logininui.html')









if __name__ == '__main__':

    app.run(debug=True)

@app.route("/")
def main():
    return redirect(url_for("login"))

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/home/")
def home():
    return render_template('home.html')

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





