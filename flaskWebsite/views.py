from flask import Blueprint #Routes
from config import app, db

#views = Blueprint('views', __name__)

@app.route('/contacts')
def get_contacts():
    return "<h1>Test</h1>"