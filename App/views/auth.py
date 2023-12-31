from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user
from App.database import db, get_migrate
from App.models import User, Student, Admin
from.index import index_views

from App.controllers import (
    create_user,
    jwt_authenticate,
    get_all_users_json,
    login,
    add_result,
    get_all_results_json,
    get_all_log_json,
    create_student,
    create_admin,
    create_competition,
    get_all_comp_json
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''

@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)


@auth_views.route('/identify', methods=['GET'])
@login_required
def identify_page():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})


@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    user = login(data['username'], data['password'])
    existing_user = User.query.filter((User.username == data['username']) & (User.password == data['password'] )).first()
    if existing_user:
        return redirect('/studentdashboard')
    return 'bad username or password given', 401

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    data = request.form
    user = login(data['username'], data['password'])
    return 'logged out!'

@auth_views.route('/studentsignup', methods=['POST'])
def signup_action():
    data = request.form
    fName = data['fName']
    lName = data['lName']
    username = data['username']
    email = data['email']
    password = data['password']
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()

    if existing_user:
        return jsonify({"error":"Username or email already taken"}), 409

    new_user = create_student(fName=fName, lName=lName, email=email,username=username, password=password)

    db.session.add(new_user)
    db.session.commit()
    return redirect('/studentdashboard')

@auth_views.route('/signup', methods=['POST'])
def student_signup_action():
    data = request.form  
    fName = data['fName']
    lName = data['lName']
    username = data['username']
    email = data['email']
    password = data['password']

    # Check if the username or email is already taken
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()

    if existing_user:
        return jsonify({"error":"Username or email already taken"}), 409

    new_student = create_student(fName=fName, lName=lName, email=email,username=username, password=password)

    db.session.add(new_student)
    db.session.commit()

    return redirect('/studentdashboard')

@auth_views.route('/adminsignup', methods=['POST'])
def admin_signup_action():
    data = request.form  
    fName = data['fName']
    lName = data['lName']
    username = data['username']
    email = data['email']
    password = data['password']

    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()

    if existing_user:
        return jsonify({"error":"Username or email already taken"}), 409


    new_admin = create_admin(fName=fName, lName=lName, email=email,username=username, password=password)

    db.session.add(new_admin)
    db.session.commit()

    return redirect('/admindashboard')
'''
API Routes
'''

@auth_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@auth_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})
    
@auth_views.route('/api/ranking', methods=['GET'])
def get_leaderboard_action():
    results = get_all_results_json()
    return jsonify(results)

@auth_views.route('/api/ranking', methods=['POST'])
def get_result_endpoint():
    data = request.json
    add_result(data['competitionID'], data['studentID'], data['position'], data['score'])
    response_data =[
    {
        "competitionID": data['competitionID'],
        "studentID": data['studentID'],
        "position": data['position'],
        "score": data['score']
    }]
    return jsonify([response_data])


@auth_views.route('/api/competitiondetails', methods=['GET'])
def get_competition_action():
    competitions = get_all_comp_json()
    return jsonify(competitions)

@auth_views.route('/api/competitiondetails', methods=['POST'])
def get_competition_endpoint():
    data = request.json
    create_competition(data['name'], data['startDate'], data['endDate'], data['division'], data['description'])
    return jsonify({'message': f"Competition {data['competitionID']} created!"})

@auth_views.route('/api/login', methods=['GET'])
def get_log_action():
    users = get_all_log_json()
    return jsonify(users)

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
  data = request.json
  token = jwt_authenticate(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  return jsonify(access_token=token)

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"username: {jwt_current_user.username}, id :{jwt_current_user.id}"})
