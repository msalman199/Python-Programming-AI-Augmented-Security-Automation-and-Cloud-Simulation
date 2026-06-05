from flask import Flask
from app.models import db
from app.config import Config

def create_app(config_class=Config):
    '''
    Application factory pattern.
    
    Args:
        config_class: Configuration class to use
    
    Returns:
        Configured Flask application
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # TODO: Initialize database with app
    # TODO: Import and register routes blueprint
    # TODO: Create tables within app context
    
    return app
