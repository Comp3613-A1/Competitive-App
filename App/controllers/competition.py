from App.models import Competition
from App.database import db

def create_competition(self, competitionID, studentID, position, score):
    newcompetition = Competition(staffID=staffID, name=name, startDate=startDate, endDate=endDate, division=division, description=description)
    db.session.add(newcompetition)
    db.session.commit()
    return newcompetition