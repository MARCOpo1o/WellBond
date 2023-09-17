from app import db

class Elder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    biometric_data = db.Column(db.String(1000))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hours_volunteered = db.Column(db.Integer)
