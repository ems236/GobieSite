from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://webappuser:scwruHead2@localhost/Gobies'
db = SQLAlchemy(app)

from app import routes