from datetime import datetime

from flask import render_template
from flask_login import login_required, current_user

from app import app, db


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.before_request
def update_last_users_login():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()