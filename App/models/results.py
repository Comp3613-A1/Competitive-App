from App.models import *
from App.database import db

class Results(db.Model):
    __tablename__ = 'Results'
    results_id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.competitionID'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, competition_id, student_id, position, score):
        self.competition_id = competition_id
        self.student_id = student_id
        self.position = position
        self.score = score
