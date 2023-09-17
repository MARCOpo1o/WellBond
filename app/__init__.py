from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Replace with your database configuration
db = SQLAlchemy(app)

from app import routes  # Import routes after db to avoid circular import
