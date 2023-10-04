from App.models import *
from App.database import db

class Student(db.Model):
    __tablename__ = 'Student'
    studentID = db.Column(db.Integer,  primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False, unique = False)
    
    def __init__(self, studentID, user_id):
        self.studentID = studentID
        self.user_id = user_id
    
    def view_competition_details(self, competition_identifier):
        # Assuming you have a relationship between Student and Competition models,
        # you can access the competitions associated with this student.

        # Check if the competition_identifier is an integer (ID)
        if isinstance(competition_identifier, int):
            # Query by competition ID
            competition = Competition.query.filter_by(id=competition_identifier, student_id=self.studentID).first()
        else:
            # Query by competition name 
            competition = Competition.query.filter_by(name=competition_identifier, student_id=self.studentID).first()

        return competition
