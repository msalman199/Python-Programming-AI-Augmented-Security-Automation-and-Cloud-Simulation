from flask import Flask, jsonify, request
import sqlite3
from datetime import datetime
import json

app = Flask(__name__)
DB_PATH = 'jobs.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/jobs', methods=['GET'])
def get_jobs():
    """Retrieve all jobs or filter by status"""
    status = request.args.get('status')
    conn = get_db_connection()
    
    if status:
        jobs = conn.execute('SELECT * FROM jobs WHERE status = ?', (status,)).fetchall()
    else:
        jobs = conn.execute('SELECT * FROM jobs').fetchall()
    
    conn.close()
    return jsonify([dict(job) for job in jobs])

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """Retrieve a specific job by ID"""
    conn = get_db_connection()
    job = conn.execute('SELECT * FROM jobs WHERE id = ?', (job_id,)).fetchone()
    conn.close()
    
    if job is None:
        return jsonify({'error': 'Job not found'}), 404
    
    return jsonify(dict(job))

@app.route('/jobs/<int:job_id>/status', methods=['PUT'])
def update_job_status(job_id):
    """
    Update job status and optionally store results
    
    Expected JSON body:
    {
        "status": "processing|completed|failed",
        "result": "optional result data"
    }
    """
    # TODO: Extract status and result from request JSON
    # TODO: Validate that status is one of: pending, processing, completed, failed
    # TODO: Update the job in database with new status, result, and updated_at timestamp
    # TODO: Return updated job data or error if job not found
    pass

@app.route('/jobs', methods=['POST'])
def create_job():
    """
    Create a new job
    
    Expected JSON body:
    {
        "job_type": "backup|cleanup|report",
        "payload": "JSON string with job parameters"
    }
    """
    # TODO: Extract job_type and payload from request
    # TODO: Insert new job into database
    # TODO: Return created job with ID
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
