from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
import sys

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SECRET_KEY"] = "pakistan1234567890"
# initialize the app with the extension
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

from admin import routes