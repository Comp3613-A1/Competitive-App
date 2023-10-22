from App.models import Competition
from App.models import Results
from sqlalchemy import func, desc
from App.models import User
from App.database import db

def create_admin(fName, lName, email, username, password):
    new_admin = User(fName=fName, lName=lName, email=email,username=username, password=password)
    db.session.add(new_admin)
    db.session.commit()
    return new_admin

def get_all_comp():
    return Competition.query.all()

def create_competition( name, startDate, endDate, division, description):
    # Create a new competition and add it to the database
    competition = Competition(
        #staffID=self.staffID,self, #associates staff member with the competition they created
        name=name,
        startDate=startDate,
        endDate=endDate,
        division=division, #Add division category the competition allows
        description=description,  # Add description field for competition
    )
    db.session.add(competition)
    db.session.commit()
    return competition

def add_result(competitionID, studentID, position, score):
        
        # Store rankings before new results are added
        #prev_ranks = view_rankings()
  
        # Create a new competition result and add it to the database
        result = Results(
            competitionID=competitionID,
            studentID=studentID,
            position=position,
            score=score
        )
        db.session.add(result)
        db.session.commit()

        return result
      
        # Get the rankings after results were added
        #current_ranks = view_rankings()

        # Find users who were in the top 20 in the previous rankings
        """top_20_previous = [user for user, position in prev_ranks[:20]]

        # Find users who are in the top 20 in the current leaderboard
        top_20_current = [user for user, position in current_ranks[:20]]

        # Compare the top 20 users in the current leaderboard with the previous rankings
        for user in top_20_previous:
            if user not in top_20_current:
                # User was in the top 20 previously but not anymore, send a notification
                send_notification(user, "Your ranking has dropped out of the top 20.")
"""
        #return result

def send_notification(student, notif):
    student.add_notification(notif)
    db.session.commit()
