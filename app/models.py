from app import db

team_player = db.Table(
	'team_player',
	db.Column('teamId', db.Integer, db.ForeignKey('team.id'), primary_key=True),
	db.Column('playerId', db.Integer, db.ForeignKey('player.id'), primary_key=True),
	db.Column('nickname', db.String),
	db.Column('position', db.String),
	)

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
	players = db.relationship("Player", secondary='team_player', lazy='subquery', backref=db.backref('teams', lazy=True))

	def currentOfType(queryTypeId):
		maxYear = db.session.query(func.max(Team.springYear)).scalar()
		return getByTypeYear(queryTypeId, maxYear)

	def getByTypeYear(queryTypeId, year):
		return Team.query.filter(Team.typeId == queryTypeId, Team.springYear == year)

class Player(db.Model):
	__tablename__ = 'player'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	hometown = db.Column(db.String)
	gradYear = db.Column(db.String)
	major = db.Column(db.String)

