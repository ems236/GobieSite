from flask import Flask
from app.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://webappuser:scwruHead2@localhost/Gobies'
db.app = app
db.init_app(app)

from app import routes
