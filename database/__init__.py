import pymysql

pymysql .install_as_MySQLdb()
# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from your_flask_app import routes  # import routes at the end to avoid circular imports
