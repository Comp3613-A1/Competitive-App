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
            return jsonify({"error":"Unauthorized."}), 401
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


def add_result(competitionID, studentID, position, score):
        
        # Store rankings before new results are added
        #prev_ranks = view_rankings()
  
        # Create a new competition result and add it to the database
        result = Results(
            competitionID=competitionID,
            studentID=studentID,
            position=position,
            score=score
        )
        db.session.add(result)
        db.session.commit()

        return result
      
        # Get the rankings after results were added
        #current_ranks = view_rankings()

        # Find users who were in the top 20 in the previous rankings
        """top_20_previous = [user for user, position in prev_ranks[:20]]

        # Find users who are in the top 20 in the current leaderboard
        top_20_current = [user for user, position in current_ranks[:20]]

        # Compare the top 20 users in the current leaderboard with the previous rankings
        for user in top_20_previous:
            if user not in top_20_current:
                # User was in the top 20 previously but not anymore, send a notification
                send_notification(user, "Your ranking has dropped out of the top 20.")
"""
        #return result

@admin_views.route('/addresults', methods=['POST'])
def get_results_action():

try:
    data = request.form 
    competitionID = data['competitionID']
    studentID = data['studentID']
    position = data['position']
    score = data['score']
    new_results = add_result(competitionID=competitionID, studentID=studentID, position=position, score=score)
    db.session.add(new_results)
    db.session.commit()
except Exception as e:
        return jsonify({'error': str(e)}), 200
return redirect('/ranking')
    #return get_all_results_json()
    #return jsonify(message=f'{new_results.competitionID}')
    # Redirect to a success page or return a JSON response
   # return redirect('/studentdashboard') get_result_json
    #jsonify(message=f'User {new_user.id} - {new_user.username} created!'), 201

@admin_views.route('/api/results', methods=['GET'])
def get_results_json_action():
    results = get_all_results_json()
    return jsonify(results)

@admin_views.route('/api/results', methods=['POST'])
def get_results_endpoint():
    data = request.json
    add_result(data['competitionID'],data['studentID'], data['position'],data['score'])
    return jsonify({'message': f"new competition with id of {data['competitionID']} created"}), 201

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
    
    return get_all_comp_json()


@admin_views.route('/test_add_results', methods=['POST'])
def test_add_results():
    data = {
        'competitionID': 1,
        'studentID': 2,
        'position': 1,
        'score': 95
    }
    with admin_views.test_client() as client:
        response = client.post('/addresults', data=data)
    return response.get_data()
    
@admin_views.route('/test_add_competition', methods=['POST'])
def test_add_competition():
    data = {
        'name': 'Test Competition',
        'startDate': '2023-10-26',
        'endDate': '2023-11-01',
        'division': 'Test Division',
        'description': 'A test competition'
    }
    with admin_views.test_client() as client:
        response = client.post('/addcompetition', data=data)
    return response.get_data()
