import requests
import time
import json
import subprocess
import os
from datetime import datetime

API_BASE_URL = 'http://localhost:5000'
POLL_INTERVAL = 5  # seconds

class JobWorker:
    """Worker service that fetches and executes jobs"""
    
    def __init__(self, api_url):
        self.api_url = api_url
        self.running = True
    
    def fetch_pending_jobs(self):
        """
        Fetch jobs with 'pending' status from the API
        
        Returns:
            list: List of pending jobs
        """
        # TODO: Make GET request to /jobs?status=pending
        # TODO: Return the list of jobs or empty list on error
        pass
    
    def update_job_status(self, job_id, status, result=None):
        """
        Update job status via API
        
        Args:
            job_id: Job ID to update
            status: New status (processing, completed, failed)
            result: Optional result data
        """
        # TODO: Make PUT request to /jobs/{job_id}/status
        # TODO: Send status and result in JSON body
        # TODO: Handle response and errors
        pass
    
    def execute_backup_job(self, payload):
        """
        Execute a backup job
        
        Args:
            payload: JSON string with backup parameters
            
        Returns:
            dict: Result with success status and message
        """
        # TODO: Parse payload JSON
        # TODO: Simulate backup operation (create a tar archive or simple file copy)
        # TODO: Return success/failure result
        # Example: Use subprocess to run tar command or cp command
        pass
    
    def execute_cleanup_job(self, payload):
        """
        Execute a cleanup job
        
        Args:
            payload: JSON string with cleanup parameters
            
        Returns:
            dict: Result with files cleaned and message
        """
        # TODO: Parse payload JSON
        # TODO: Simulate cleanup (find and remove old files)
        # TODO: Return result with count of files processed
        pass
    
    def execute_report_job(self, payload):
        """
        Execute a report generation job
        
        Args:
            payload: JSON string with report parameters
            
        Returns:
            dict: Result with report data
        """
        # TODO: Parse payload JSON
        # TODO: Generate a simple system report (disk usage, memory, etc.)
        # TODO: Return report data as dictionary
        pass
    
    def process_job(self, job):
        """
        Process a single job based on its type
        
        Args:
            job: Job dictionary from API
        """
        job_id = job['id']
        job_type = job['job_type']
        payload = job['payload']
        
        print(f"[{datetime.now()}] Processing job {job_id} ({job_type})")
        
        # Update status to processing
        self.update_job_status(job_id, 'processing')
        
        try:
            # Execute job based on type
            if job_type == 'backup':
                result = self.execute_backup_job(payload)
            elif job_type == 'cleanup':
                result = self.execute_cleanup_job(payload)
            elif job_type == 'report':
                result = self.execute_report_job(payload)
            else:
                raise ValueError(f"Unknown job type: {job_type}")
            
            # Update status to completed
            self.update_job_status(job_id, 'completed', json.dumps(result))
            print(f"[{datetime.now()}] Job {job_id} completed successfully")
            
        except Exception as e:
            # Update status to failed
            error_result = {'error': str(e)}
            self.update_job_status(job_id, 'failed', json.dumps(error_result))
            print(f"[{datetime.now()}] Job {job_id} failed: {e}")
    
    def run(self):
        """Main worker loop"""
        print(f"Worker service started. Polling every {POLL_INTERVAL} seconds...")
        
        while self.running:
            try:
                # Fetch pending jobs
                jobs = self.fetch_pending_jobs()
                
                if jobs:
                    print(f"Found {len(jobs)} pending job(s)")
                    for job in jobs:
                        self.process_job(job)
                else:
                    print(f"[{datetime.now()}] No pending jobs")
                
                # Wait before next poll
                time.sleep(POLL_INTERVAL)
                
            except KeyboardInterrupt:
                print("\nShutting down worker service...")
                self.running = False
            except Exception as e:
                print(f"Error in worker loop: {e}")
                time.sleep(POLL_INTERVAL)

if __name__ == '__main__':
    worker = JobWorker(API_BASE_URL)
    worker.run()
