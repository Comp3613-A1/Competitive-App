from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user
from functools import wraps
from App.controllers import *



student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/viewprofile', methods=['GET'])
def view_student_profile():

    # if you want to hard code to test a certain user ID just change "current_user.userID" 
    # change it to the id of the student u want to see the profile of, change it lower down too 
    # around line 21
    student = Student.query.filter_by(userID=current_user.userID).first()
    print(f'current_user: {current_user}')
    if student:
        # Fetch the user object associated with the student
        user = User.query.get(current_user.userID)
        print(f'user: {user}')
        if user:
            return render_template('viewprofile.html', user=user)
        else:
            return jsonify({"error": "User not found."}), 404
    else:
        return jsonify({"error": "Student not found."}), 404

@student_views.route('/competitiondetails', methods=['GET'])
def view_competition_details(competition_identifier):
    student = Student.query.filter_by(user_id=current_user.userID).first()
    if student:
        competition = student.view_competition_details(competition_identifier)
        if competition:
            return render_template('competitiondetails.html', competition=competition)
        else:
            return "Competition not found", 404
    else:
        return jsonify({"error":"Student not found."}), 404
