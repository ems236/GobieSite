from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://webappuser:scwruHead2@localhost/Gobies'
db = SQLAlchemy(app)

from app import routes