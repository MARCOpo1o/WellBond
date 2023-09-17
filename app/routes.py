from flask import render_template, redirect, url_for
from app import app, db
from app.models import Elder, Student

@app.route('/')
def index():
    # return render_template('index.html')
    return "Hello, World!"

@app.route('/dashboard')
def dashboard():
    # Get data from DB
    return render_template('dashboard.html')
