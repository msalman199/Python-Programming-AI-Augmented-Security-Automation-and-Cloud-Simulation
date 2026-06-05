import pytest
from app import create_app
from app.models import db, JobHistory
from app.config import TestConfig
from datetime import datetime

@pytest.fixture
def app():
    '''Create application for testing'''
    app = create_app(TestConfig)
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    '''Create test client'''
    return app.test_client()

@pytest.fixture
def sample_jobs(app):
    '''Create sample job data for tests'''
    with app.app_context():
        jobs = [
            JobHistory(
                job_name='backup-db',
                status='success',
                user='admin',
                environment='prod',
                start_time=datetime(2024, 1, 15, 10, 0),
                end_time=datetime(2024, 1, 15, 10, 5),
                duration=300
            ),
            JobHistory(
                job_name='deploy-app',
                status='failed',
                user='devops',
                environment='staging',
                start_time=datetime(2024, 1, 15, 11, 0),
                end_time=datetime(2024, 1, 15, 11, 2),
                duration=120,
                error_message='Connection timeout'
            ),
            JobHistory(
                job_name='run-tests',
                status='running',
                user='jenkins',
                environment='dev',
                start_time=datetime(2024, 1, 15, 12, 0)
            )
        ]
        # TODO: Add jobs to database and commit
        return jobs
