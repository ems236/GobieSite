from app import db

class TeamType(db.Model):
	__tablename__ = 'teamType'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	shortName = db.Column(db.String(15))
	teams = db.relationship("Team", backref="type", lazy=False)

class Team(db.Model):
	__tablename__ = 'team'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(35))
	imageFileName = db.Column(db.String(60))
	springYear = db.Column(db.Integer)
	typeId = db.Column(db.Integer, db.ForeignKey('teamType.id'))
	team_players = db.relationship("Player", backref="team", lazy=False)

	def currentOfType(queryTypeId):
		maxYear =  db.session.query(db.func.max(Team.springYear)).filter(Team.typeId == queryTypeId).scalar()
		return Team.getByTypeYear(queryTypeId, maxYear)

	def getByTypeYear(queryTypeId, year):
		return Team.query.filter(Team.typeId == queryTypeId, Team.springYear == year).first()

class Player(db.Model):
	__tablename__ = 'player'
	id = db.Column(db.Integer, primary_key=True)
	teamId = db.Column(db.Integer, db.ForeignKey('team.id'))
	nickname = db.Column(db.String(30))
	position = db.Column(db.String(15))
	firstname = db.Column(db.String(30))
	hometown = db.Column(db.String(30))
	gradYear = db.Column(db.String(10))
	major = db.Column(db.String(30))
	lastname = db.Column(db.String(30))
	imageFileName = db.Column(db.String(60))

	def printName(self):
		return self.firstname.decode("utf-8") + " \"" + self.nickname.decode("utf-8") + "\" " + self.lastname.decode("utf-8")
