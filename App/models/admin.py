from App.models import *
from App.database import db

class Admin(db.Model):
    __tablename__ = 'Admin'
    staffID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=False)
    
    def __init__(self, staffID, user_id):
        self.staffID = staffID
        self.user_id = user_id

    def create_competition(self, competition_name, start_date, end_date, division, description):
        # Create a new competition and add it to the database
        competition = Competition(
            staffID=self.staffID,
            name=competition_name,
            startDate=start_date,
            endDate=end_date,
            division=division,
            description=description  # Add description field
        )
        db.session.add(competition)
        db.session.commit()
        return competition