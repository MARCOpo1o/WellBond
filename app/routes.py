from flask import render_template
from app import app  # Import the app instance from the __init__.py file

@app.route('/')
def index():
    return render_template('main_page.html')  # Use the correct template name

# @app.route('/patients')
# def dashboard():
#     # Get data from DB (You may want to retrieve data from the database here)
#     return render_template('main_page.html')  # Use the correct template name
