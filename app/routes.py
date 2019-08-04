from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

@app.route('/social')
def social():
	return render_template("social.html")

@app.route('/calendar')
def calendar():
	return render_template("calendar.html")

@app.route('/gum')
def gum():
	return render_template("gum.html")

@app.route('/about')
def about():
	return render_template("about.html")