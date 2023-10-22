from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user
from functools import wraps
from App.models import Results
from App.models import Competition
from.index import index_views
from App.database import db
#from App.controllers import *
from App.controllers import (
    create_user,
    create_competition,
    add_result,
    jwt_authenticate, 
    get_all_results_json,
    get_all_comp_json,
    get_all_users,
    get_all_users_json,
    jwt_required,
    view_ranking
)

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Admin):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

'''@admin_views.route('/competitiondetails', methods=['GET'])
def get_comp_action():
    comp = get_all_comp()
    return render_template('users.html', users=comp)'''


''' @admin_views.route('/admin/create_competition', methods=['POST'])
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
#@admin_required  
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
    return redirect(url_for('addresults.html'))"""

@admin_views.route('/addresults', methods=['POST'])
def get_results_action():
    data = request.form  # Assuming you are sending form data
    competitionID = data['competitionID']
    studentID = data['studentID']
    position = data['position']
    score = data['score']

    # Add result details
    new_results = add_result(competitionID=competitionID, studentID=studentID, position=position, score=score)

    # Add the results to the database
    db.session.add(new_results)
    db.session.commit()
    
    return get_all_results_json()
    #return jsonify(message=f'{new_results.competitionID}')
    # Redirect to a success page or return a JSON response
   # return redirect('/studentdashboard') get_result_json
    #jsonify(message=f'User {new_user.id} - {new_user.username} created!'), 201'''

@admin_views.route('/addcompetition', methods=['POST'])
def get_competition_action():
    data = request.form  # Assuming you are sending form data
    name = data['name']
    startDate= data['startDate']
    endDate= data['endDate']
    division = data['division']
    description = data['description']

    # Add result details
    new_competition = create_competition(name=name, startDate=startDate,endDate=endDate, division=division, description=description)

    # Add the results to the database
    db.session.add(new_competition)
    db.session.commit()
    
    return get_all_comp_json()
