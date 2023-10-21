
"""
This module contains functions related to student operations.
"""
from sqlalchemy import desc
#from sqlalchemy import func
from App.models.user import User
from App.models.student import Student
from App.models.competition import Competition
from App.models.results import Results
from App.database import db

stmt = db.session.query(Student).order_by(desc(Student.score))


def create_student(fName, lName, email, username, password):
    """
    Create a new student with the provided details.
    Returns the newly created student object.
    """
    new_student = User(fName=fName, lName=lName, email=email,username=username, password=password)
    db.session.add(new_student)
    db.session.commit()
    return new_student

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
def student_competitions(self):
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
        'Score': self.score,
        'Notifications': self.notification,
    }
    return profile_data
