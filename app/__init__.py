from flask import Flask
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://webappuser:scwruHead2@localhost/Gobies'
db.init_app(app)

from app import routes