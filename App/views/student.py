from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user
from functools import wraps
from App.controllers import *



student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/viewprofile', methods=['GET'])
def view_student_profile():

    student = Student.query.filter_by(userID=2).first()
    if student:

        user = User.query.get(2)

        if user:
            flash(f"Notification that you are in top 20!")
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
