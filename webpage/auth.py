from flask import * 
from .models import User, Task
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import *

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('em')
        password = request.form.get('pwd')
        user = User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password, password):
                login_user(user=user, remember=True)
                flash("Logged in successfully!", category="success")
                return redirect(url_for("views.todos"))
            else:
                flash("Incorrect email or password!", category="error")
        else:
            flash("Incorrect email or password!", category="error")
    return render_template('login.html', user=current_user)

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form.get('em')
        username = request.form.get('usr')
        password1 = request.form.get('pwd')
        password2 = request.form.get('pwd2')
        if User.query.filter_by(email=email).first():
            flash("There already exists an account with this email!", category="error")
        elif len(email)< 4 or len(username) < 2:
            flash("Email or username too short!", category="error")
        elif password1 != password2:
            flash("Passwords don't match!", category="error")
        elif len(password1)< 4 or len(password2) < 2:
            flash("Password too short!", category="error")
        else:
            user = User(email=email, password=generate_password_hash(password1), username=username)
            db.session.add(user)
            db.session.commit()
            flash("Account created successfully!", category="success")
            redirect(url_for("views.home"))

    return render_template('register.html', user=current_user)

@login_required
@auth.route('/logout/')
def logout():
    logout_user()
    flash("Logged out successfully!", category="success")
    return redirect(url_for("auth.login"))