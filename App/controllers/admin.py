from App.models import Competition
from App.models import Results
from sqlalchemy import func, desc
from App.models import User, Admin
from App.database import db

def create_admin(fName, lName, email, username, password):
    new_admin = Admin(fName=fName, lName=lName, email=email,username=username, password=password)
    db.session.add(new_admin)
    db.session.commit()
    return new_admin

def get_all_comp():
    return Competition.query.all()

def create_competition(name, startDate, endDate, division, description):
    competition = Competition(
        name=name,
        startDate=startDate,
        endDate=endDate,
        division=division,
        description=description,  
    )
    db.session.add(competition)
    db.session.commit()
    return competition

def add_result(competitionID, studentID, position, score):
        result = Results(
            competitionID=competitionID,
            studentID=studentID,
            position=position,
            score=score
        )
        db.session.add(result)
        db.session.commit()

        return result

def send_notification(student, notif):
    student.add_notification(notif)
    db.session.commit()
