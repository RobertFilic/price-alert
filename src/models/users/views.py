from flask import Blueprint, request, session, url_for, render_template, redirect
from src.models.users.user import User
import src.models.users.errors as UserErrors

#from werkzeug.utils import redirect


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login', methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        # check user/password combo
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_login_vlaid(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))

        except UserErrors.UserError as e:
            return e.message

    render_template('/users/login.html') # Possible improvements: send the user an error if the Login is invalid


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == "POST":
        # check user/password combo
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))

        except UserErrors.UserError as e:
            return e.message

    render_template('/users/register.html') # Possible improvements: send the user an error if the Login is invalid


@user_blueprint.route('/alerts')
def user_alerts():
    return "This is the alerts page"


@user_blueprint.route('/logout')
def logout_user():
    pass


@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass
