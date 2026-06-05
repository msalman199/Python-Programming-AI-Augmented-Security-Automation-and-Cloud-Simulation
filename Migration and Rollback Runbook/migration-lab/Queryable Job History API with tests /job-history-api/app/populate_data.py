from app import create_app
from app.models import db, JobHistory
from datetime import datetime, timedelta
import random

def populate_sample_data():
    '''Create sample job history data for testing'''
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        job_names = ['backup-database', 'deploy-app', 'run-tests', 'cleanup-logs']
        statuses = ['success', 'failed', 'running']
        environments = ['dev', 'staging', 'prod']
        users = ['admin', 'devops', 'jenkins']
        
        # TODO: Create 20-30 sample job entries
        # Use random choices from lists above
        # Vary start_time over past 7 days
        # Set end_time and duration for completed jobs
        # Add error_message for failed jobs
        
        print(f"Created sample job history entries")

if __name__ == '__main__':
    populate_sample_data()
