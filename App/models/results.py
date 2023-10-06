from App.models import *
from App.database import db

class Results(db.Model):
    __tablename__ = 'Results'
    resultsID = db.Column(db.Integer, primary_key=True)
    competitionID = db.Column(db.Integer, db.ForeignKey('competition.competitionID'), nullable=False)
    studentID = db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, competitionID, studentID, position, score):
        self.competitionID = competitionID
        self.studentID = studentID
        self.position = position
        self.score = score
