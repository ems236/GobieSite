from flask import render_template, abort
from app.models import Team, TeamType, Player
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

@app.route('/cwrul')
def cwrul():
	return render_template("cwrul.html")

@app.route('/northcoast')
def northcoast():
	return render_template("northcoast.html")

@app.route('/team/<type>')
@app.route('/team/<type>/<int:year>')
def team(typeShortname, year=None):
	teamType = TeamType \
		.query \
		.filter(TeamType.shortName == typeShortname) \
		.first()

	if(teamType is None):
		return abort(404)

	team = None
	if(year is None):
		team = Team.currentOfType(teamType.id)
	else:
		team = Team.getByTypeYear(teamType.id, year)

	if(team is None):
		return abort(404)

	return render_template("test.html", team=team)