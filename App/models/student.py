from App.models import *
from App.database import db

class Student(db.Model):
    __tablename__ = 'Student'
    studentID = db.Column(db.Integer,  primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable = False, unique = False)
    
    def __init__(self, studentID, user_id):
        self.studentID = studentID
        self.user_id = user_id
    
    def view_competition_details(self, competition_identifier):
        #Check if the competition_identifier is an integer (ID)
        if isinstance(competition_identifier, int):
            #Query by competition ID
            competition = Competition.query.filter_by(id=competition_identifier, student_id=self.studentID).first()
        else:
            #Query by competition name 
            competition = Competition.query.filter_by(name=competition_identifier, student_id=self.studentID).first()

        return competition

    #Get a list of competitions that the specific Student participated in
    def user_competitions(self):
        # Query competitions where the student's ID matches the 'student_id' in Results
        competitions = Competition.query.join(Results).filter(Results.student_id == self.studentID).all()
        
        return competitions

    def view_profile(self):
        # Query the user associated with this student
        user = User.query.get(self.user_id)

        profile_data = {
            'First Name': user.fName,
            'Last Name': user.lName,
            'Email': user.email,
            'Username': user.username,
        }

        return profile_data