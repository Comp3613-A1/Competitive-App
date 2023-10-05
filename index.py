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

@index_views.route('/studentlogin', methods=['GET'])
def student_login_page():
    return render_template('studentlogin.html')

@index_views.route('/studentsignup', methods=['GET'])
def student_signup_page():
    return render_template('studentsignup.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})