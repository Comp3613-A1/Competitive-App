from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/adminlogin', methods=['GET'])
def admin_login_page():
    return render_template('adminlogin.html')

@index_views.route('/adminsignup', methods=['GET'])
def admin_signup_page():
    return render_template('adminsignup.html')

@index_views.route('/admindashboard', methods=['GET'])
def admin_dashboard():
    return render_template('admindashboard.html')

@index_views.route('/addcompetition', methods=['GET'])
def addcompetition():
    return render_template('/addcompetition.html')

@index_views.route('/studentlogin', methods=['GET'])
def student_login_page():
    return render_template('studentlogin.html')

@index_views.route('/studentsignup', methods=['GET'])
def student_signup_page():
    return render_template('studentsignup.html')

@index_views.route('/studentdashboard', methods=['GET'])
def student_dashboard():
    return render_template('studentdashboard.html')

@index_views.route('/viewprofile', methods=['GET'])
def view_profile():
    return render_template('viewprofile.html')

@index_views.route('/competitiondetails', methods=['GET'])
def competitiondetails():
    return render_template('competitiondetails.html')

@index_views.route('/ranking', methods=['GET'])
def ranking_page():
    return render_template('ranking.html')

@index_views.route('/addresults', methods=['GET'])
def add_results():
    return render_template('addresults.html')

@index_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'lastbob', 'bob123@bob.com','bobuser', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
