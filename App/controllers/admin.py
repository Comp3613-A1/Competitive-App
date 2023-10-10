from App.database import db
from App.models import Competition

def create_competition(self, competition_name, start_date, end_date, division, description):
    # Create a new competition and add it to the database
    competition = Competition(
        staffID=self.staffID, #associates staff member with the competition they created
        name=competition_name,
        startDate=start_date,
        endDate=end_date,
        division=division, #Add division category the competition allows
        description=description,  # Add description field for competition
    )
    db.session.add(competition)
    db.session.commit()
    return competition

def add_result(competition_id, student_id, position, score):
        
        # Store rankings before new results are added
        prev_ranks = view_rankings()
  
        # Create a new competition result and add it to the database
        result = Result(
            competition_id=competition_id,
            student_id=student_id,
            position=position,
            score=score
        )
        db.session.add(result)
        db.session.commit()
      
        # Get the rankings after results were added
        current_ranks = view_rankings()

        # Find users who were in the top 20 in the previous rankings
        top_20_previous = [user for user, position in prev_ranks[:20]]

        # Find users who are in the top 20 in the current leaderboard
        top_20_current = [user for user, position in current_ranks[:20]]

        # Compare the top 20 users in the current leaderboard with the previous rankings
        for user in top_20_previous:
            if user not in top_20_current:
                # User was in the top 20 previously but not anymore, send a notification
                send_notification(user, "Your ranking has dropped out of the top 20.")

        return result

def send_notification(student, notif):
    student.add_notification(notif)
    db.session.commit()
