from App.database import db
from App.models import *
class Competition(db.Model):
    __tablename__ = 'Competition'
    competitionID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    startDate = db.Column(db.String, unique=False, nullable=False)
    endDate = db.Column(db.String, unique=False, nullable=False)
    division = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(255))  # Add a description field

    def __init__(self, name, startDate, endDate, division, description):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.division = division
        self.description = description

    def get_json(self):
        return{
            'id': self.competitionID,
            'name': self.name,
            'Start Date': self.startDate,
            'End Date': self.endDate,
            'Division': self.division,
            'Description': self.description
        }
