#imports flask sync test
from flask import Flask
#Imports templates so we can use html
from flask import render_template
from flask import request
from flask import redirect, url_for, session, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login_app.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# class 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

# The logot thing
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

@app.route("/")
def main():
    return render_template('main.html')

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





