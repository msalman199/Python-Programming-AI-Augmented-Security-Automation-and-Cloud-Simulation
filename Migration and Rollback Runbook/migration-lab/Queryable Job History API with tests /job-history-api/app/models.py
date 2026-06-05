from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class JobHistory(db.Model):
    '''
    Model for storing job execution history.
    '''
    __tablename__ = 'job_history'
    
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # success, failed, running
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)  # in seconds
    user = db.Column(db.String(50))
    environment = db.Column(db.String(20))  # dev, staging, prod
    error_message = db.Column(db.Text)
    
    def to_dict(self):
        '''
        Convert model instance to dictionary.
        
        Returns:
            Dictionary representation of job history
        '''
        # TODO: Implement conversion to dictionary
        # Include all fields, handle None values for end_time
        pass
