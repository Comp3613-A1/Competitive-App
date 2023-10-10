from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user
from functools import wraps
from App.controllers import *

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Admin):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

@admin_views.route('/admin/create_competition', methods=['POST'])
#@admin_required
def create_competition_view():
    
    # Getting form data
    competition_name = request.form.get('competition_name')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    division = request.form.get('division')
    description = request.form.get('description')

    # Creating a new competition
    #admin = Admin.query.first() 
    competition = create_competition(competition_name, start_date, end_date, division, description)

    db.session.add(competition)
    db.session.commit()
    # Redirect to another page
    return redirect ('/admindashboard')

@admin_views.route('/admin/add_result', methods=['POST'])
#@admin_required  # Decorate with your admin authorization decorator
def add_result_view():

    # Getting form data
    competition_id = request.form.get('competition_id')
    student_id = request.form.get('student_id')
    position = request.form.get('position')
    score = request.form.get('score')

    # Creating a result record
    admin = Admin.query.first()  
    result = admin.add_result(competition_id, student_id, position, score)

    # Redirect to another page
    return redirect(url_for('addresults.html'))
