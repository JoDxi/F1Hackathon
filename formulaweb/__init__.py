from flask import Flask
import flask_migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5861ca271e02884a96bc6076e9b82ed'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///formulaweb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from formulaweb.models import Teams
from formulaweb import routes
