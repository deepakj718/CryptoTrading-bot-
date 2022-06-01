from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from requests import request
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)

@main.route('/profile', methods=['POST'])
def run_trader():
    # get ticker symbol
    ticker = request.form.get('tag')

    user = User.query.filter_by(email=email).first()

   
    