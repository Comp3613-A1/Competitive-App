from App.models import *
from App.database import db

class Admin(User):
    __tablename__ = 'Admin'
    staffID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False, unique=False)
   
    def __init__(self, staffID, user_id):
        self.staffID = staffID
        self.user_id = user_id

    def create_competition(self, competition_name, start_date, end_date, division, description):
        # Create a new competition and add it to the database
        competition = Competition(
            staffID=self.staffID, #associates staff member with the competition they created
            name=competition_name,
            startDate=start_date,
            endDate=end_date,
            division=division, #Add division category the competition allows
            description=description  # Add description field for competition
        )
        db.session.add(competition)
        db.session.commit()
        return competition

    def add_result(self, competition_id, student_id, position, score):
        # Create a new competition result and add it to the database
            result = Result(
            competition_id=competition_id,
            student_id=student_id,
            position=position,
            score=score
        )
        db.session.add(result)
        db.session.commit()
        return result
