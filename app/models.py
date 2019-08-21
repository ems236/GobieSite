from app import db

class TeamPlayer(db.Model):
	__tablename__ = 'team_player'
	teamId = db.Column('teamId', db.Integer, db.ForeignKey('team.id'), primary_key=True)
	playerId = db.Column('playerId', db.Integer, db.ForeignKey('player.id'), primary_key=True)
	nickname = db.Column('nickname', db.String)
	position = db.Column('position', db.String)

	def printName(self):
		return self.player.firstname.decode("utf-8") + " \"" + self.nickname.decode("utf-8") + "\" " + self.player.lastname.decode("utf-8")

class TeamType(db.Model):
	__tablename__ = 'teamType'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	shortName = db.Column(db.String)
	teams = db.relationship("Team", backref="type", lazy=False)

class Team(db.Model):
	__tablename__ = 'team'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	imageFileName = db.Column(db.String)
	springYear = db.Column(db.Integer)
	typeId = db.Column(db.Integer, db.ForeignKey('teamType.id'))
	team_players = db.relationship("TeamPlayer", backref="team", lazy=False)

	def currentOfType(queryTypeId):
		maxYear =  db.session.query(db.func.max(Team.springYear)).filter(Team.typeId == queryTypeId).scalar()
		return Team.getByTypeYear(queryTypeId, maxYear)

	def getByTypeYear(queryTypeId, year):
		return Team.query.filter(Team.typeId == queryTypeId, Team.springYear == year).first()

class Player(db.Model):
	__tablename__ = 'player'
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String)
	hometown = db.Column(db.String)
	gradYear = db.Column(db.String)
	major = db.Column(db.String)
	lastname = db.Column(db.String)
	team_players = db.relationship("TeamPlayer", backref="player", lazy=False)