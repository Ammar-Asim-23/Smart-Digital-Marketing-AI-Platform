import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SayabiDevsTeam9'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_DRIVER = os.environ.get('DATABASE_DRIVER')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_PORT = os.environ.get("PORT")

    # Email
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'your-email@example.com'
    MAIL_PASSWORD = 'your-email-password'
    MAIL_DEFAULT_SENDER = 'your-email@example.com'

    # Other settings
    # ...

