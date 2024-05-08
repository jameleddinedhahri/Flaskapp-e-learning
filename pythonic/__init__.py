from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SECRET_KEY"]="d287c7c6b41513bf7ddeddb150bcaf9537b55096daddf3a958a20bd2690511d5"
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonic.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt()

from pythonic import routes