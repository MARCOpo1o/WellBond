from flask import render_template
from app import app  # Import the app instance from the __init__.py file

@app.route('/')
def index():
    return render_template('main_page.html')  # Use the correct template name

@app.route('/details')
def details():
    return render_template('patient_details.html')  # Use the correct template name