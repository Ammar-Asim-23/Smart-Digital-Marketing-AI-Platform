from flask import Blueprint, render_template
from models.database import Session, User
from markify import db


users_bp = Blueprint('users', __name__)



@users_bp.route('/users')
def list_users():
    
    
    session = Session()
    
    # Query the User model to get a list of users
    users = session.query(User).all()

    # Close the session
    session.close()

    # Render a template or return the data as JSON
    return render_template('users.html', users=users)
