#imports flask sync test
from flask import Flask
#Imports templates so we can use html
from flask import render_template
from flask import request
from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)



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





