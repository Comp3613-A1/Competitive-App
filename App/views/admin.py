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
def create_competition_view():
    competition_name = request.form.get('competition_name')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    division = request.form.get('division')
    description = request.form.get('description')

    # Create a new competition
    admin = Admin.query.first() 
    competition = admin.create_competition(competition_name, start_date, end_date, division, description)

    # Redirect to another page
    return redirect(url_for('competition_list'))

