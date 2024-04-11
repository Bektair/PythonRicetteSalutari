from flask import Blueprint #Routes

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>/logout</p>"

@auth.route('sign-up')
def sign_up():
    return "<p>Sign Up</p>"