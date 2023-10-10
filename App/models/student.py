from App.models import *
from App.database import db

class Student(User):
    __tablename__ = 'Student'
    studentID = db.Column(db.Integer,  primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable = False, unique = False)
    score = db.Column(db.Float, nullable = False, unique = False, default=0)
    notification = db.Column(db.String(500), nullable = False, unique = False, default = 'No Notifications.')
    
    def __init__(self, score=0, notification='No Notifications.', fName, lName, email, username, password):
        super().__init__(fName, lName, email, username, password)
        self.score = score
        self.notification = notification
   
    def add_notification(self, message):
        self.notification += f"\n{message}"
