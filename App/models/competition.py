from App.models import *
from App.database import db

class Competition(db.Model):
    __tablename__ = 'competition'
    competitionID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False, unique=False)
    name = db.Column(db.String(120), nullable=False)
    startDate = db.Column(db.String, unique=False, nullable=False)
    endDate = db.Column(db.String, unique=False, nullable=False)
    division = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(255))  # Add a description field

    def __init__(self, staffID, name, startDate, endDate, division, description):
        self.staffID = staffID
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.division = division
        self.description = description