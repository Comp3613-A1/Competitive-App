from App.models import *
from App.database import db

class Student(db.Model):
    __tablename__ = 'Student'
    studentID = db.Column(db.Integer,  primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False, unique = False)
    
    def __init__(self, studentID, user_id):
        self.studentID = studentID
        self.user_id = user_id
        