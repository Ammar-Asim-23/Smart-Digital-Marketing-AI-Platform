from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from routes.user_routes import users_bp  # Import the users Blueprint
from routes.campaign_routes import campaigns_bp




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(campaigns_bp, url_prefix='/campaigns')    


if __name__ == '__main__':
    app.run(debug=True)