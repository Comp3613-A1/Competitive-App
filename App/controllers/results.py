from App.models import Results
from App.database import db

def create_result(self, competitionID, studentID, position, score):
    newresult = Result(competitionID=competitionID, studentID=studentID, position=position,score=score)
    db.session.add(newuser)
    db.session.commit()
    return newresult