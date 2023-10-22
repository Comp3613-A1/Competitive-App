from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views
from App.controllers import *
from App.models import User

from App.controllers import (
    create_user,
    jwt_authenticate, 
    get_all_users,
    get_all_users_json,
    jwt_required,
    view_ranking,
    get_all_results
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/student/leaderboard', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['fName'],data['lName'], data['email'],data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/ranking', methods=['GET'])
def view_leaderboard():
    leaderboard=get_all_results()
    return render_template('ranking.html', leaderboard=leaderboard)

'''
@user_views.route('/leaderboard', methods=['GET'])
def view_leaderboard():
    student = Student.query.filter_by(user_id=current_user.userID).first()
    if student:
        leaderboard=view_ranking()
        return render_template('leaderboard.html', leaderboard=leaderboard)
        '''