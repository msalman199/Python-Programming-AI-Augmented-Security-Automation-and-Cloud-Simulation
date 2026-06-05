#!/usr/bin/env python3
from job_manager import JobManager
import time

def test_job_lifecycle():
    """Test complete job lifecycle."""
    manager = JobManager()
    
    # TODO: Create a new job named "data_processing_job"
    
    # TODO: Print job_id and initial status
    
    # TODO: Start the job
    
    # TODO: Simulate work with time.sleep(2)
    
    # TODO: Complete job with sample results
    # Sample result: {"records_processed": 1500, "errors": 0}
    
    # TODO: Retrieve and print final job status
    
    # TODO: Calculate and print job duration
    
    manager.close()

def test_failed_job():
    """Test job failure scenario."""
    manager = JobManager()
    
    # TODO: Create a new job named "failing_job"
    
    # TODO: Start the job
    
    # TODO: Fail the job with error message
    
    # TODO: Retrieve and print job status
    
    manager.close()

def test_query_by_status():
    """Test querying jobs by status."""
    manager = JobManager()
    
    # TODO: Query all completed jobs
    
    # TODO: Print count and details
    
    # TODO: Query all failed jobs
    
    # TODO: Print count and details
    
    manager.close()

if __name__ == "__main__":
    print("Testing Job Lifecycle...")
    test_job_lifecycle()
    
    print("\nTesting Failed Job...")
    test_failed_job()
    
    print("\nTesting Query by Status...")
    test_query_by_status()
