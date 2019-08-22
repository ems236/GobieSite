from flask import render_template, abort
from app.models import Team, TeamType, Player
from app import app

#creates data for roster dropdown
@app.context_processor
def inject_teamTypes():
	return dict(types=TeamType.query.all())

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

@app.route('/team/<typeShortName>')
@app.route('/team/<typeShortName>/<int:year>')
def team(typeShortName, year=None):
	teamType = TeamType \
		.query \
		.filter(TeamType.shortName == typeShortName) \
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

	return render_template("team.html", team=team)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
