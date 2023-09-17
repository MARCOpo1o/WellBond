from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database file will be site.db
db = SQLAlchemy(app)

from app import routes  # Import routes after db to avoid circular import
