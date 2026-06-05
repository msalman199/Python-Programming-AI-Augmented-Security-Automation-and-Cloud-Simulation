-- TODO: Create jobs table with appropriate columns
CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    job_name VARCHAR(255) NOT NULL,
    -- TODO: Add status column (pending, running, completed, failed)
    -- TODO: Add created_at timestamp
    -- TODO: Add started_at timestamp (nullable)
    -- TODO: Add completed_at timestamp (nullable)
    -- TODO: Add result_data JSONB column for storing results
    -- TODO: Add error_message TEXT column (nullable)
);

-- TODO: Create index on job_name for faster lookups

-- TODO: Create index on status for filtering queries

-- TODO: Create index on created_at for time-based queries
