from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    userID = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(100), nullable=False, unique=True)
    fName = db.Column(db.String(100), nullable=False)
    lName = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    

    def __init__(self, fName, lName, email, username, password):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.userID,
            'firstName': self.fName,
            'lastName': self.lName,
            'email': self.email,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    @classmethod
    def view_ranking(cls):
        # Query all students and order them by score (in descending order) to create the leaderboard
        leaderboard = (
            db.session.query(cls, func.row_number().over(order_by=desc(cls.score)).label("position"))
            .order_by(desc(cls.score))
            .all()
        )
        return leaderboard
