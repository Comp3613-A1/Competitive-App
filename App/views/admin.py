from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user
from functools import wraps
from App.models import Results
from App.models import Competition
from.index import index_views
from App.database import db
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
            return jsonify({"error":"Unauthorized."}), 401
        return func(*args, **kwargs)
    return wrapper

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

@admin_views.route('/addresults', methods=['POST'])
def get_results_action():
    #try:
    data = request.form 
    competitionID = data['competitionID']
    studentID = data['studentID']
    position = data['position']
    score = data['score']
    new_results = add_result(competitionID=competitionID, studentID=studentID, position=position, score=score)
    db.session.add(new_results)
    db.session.commit()
    results = get_all_results_json() 
    return jsonify({
        'message': 'Results successfully created!',
        'results': results 
    })  
    

@admin_views.route('/addcompetition', methods=['POST'])
def get_competition_action():
    data = request.form  
    name = data['name']
    startDate= data['startDate']
    endDate= data['endDate']
    division = data['division']
    description = data['description']
    new_competition = create_competition(name=name, startDate=startDate,endDate=endDate, division=division, description=description)
    db.session.add(new_competition)
    db.session.commit()
    competitions = get_all_comp_json() 
    return jsonify({
        'message': 'Competition successfully created!',
        'competitions': competitions 
    })  
