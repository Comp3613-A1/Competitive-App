from sqlalchemy import func, desc
from App.models import User
from App.database import db

def create_user(fName, lName, email, username, password):
    newuser = User(fName=fName, lName=lName, email=email,username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(userID):
    return User.query.get(userID)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def get_all_log_json():
    users = User.query.all()
    if not users:
        return []
    user_list = []
    for user in users:
        user_data = {
            'username': user.username,
            'password': user.password,
        }
        user_list.append(user_data)
    return user_list

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def view_ranking():
    # Query all students and order them by score (in descending order) to create leaderboard
    leaderboard = (
        db.session.query(cls, func.row_number().over(order_by=desc(cls.score)).label("position"))
        .order_by(desc(cls.score))
        .all()
    )
    return leaderboard
