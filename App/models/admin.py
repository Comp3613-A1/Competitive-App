from App.models import *
from App.database import db

class Admin(User):
    __tablename__ = 'Admin'
    staffID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False, unique=False)
   
    def __init__(self, fName, lName, email, username, password):
        super().__init__(fName, lName, email, username, password)
        
