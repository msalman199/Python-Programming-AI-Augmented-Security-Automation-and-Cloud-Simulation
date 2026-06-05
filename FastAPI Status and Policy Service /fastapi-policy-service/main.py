from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import Dict
import psutil

from models import SystemStatus, PolicyCheckRequest, PolicyCheckResponse, HealthResponse
from policies import check_system_health, validate_request_size, validate_http_method, enforce_rate_limit
from config import API_CONFIG

app = FastAPI(
    title=API_CONFIG["title"],
    version=API_CONFIG["version"],
    description=API_CONFIG["description"]
)

# In-memory storage for rate limiting (use Redis in production)
request_tracker: Dict[str, int] = {}

@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint - basic health check"""
    # TODO: Return HealthResponse with current timestamp and status
    pass

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Detailed health check endpoint"""
    # TODO: Implement health check logic
    # TODO: Return appropriate response
    pass

@app.get("/status", response_model=SystemStatus)
async def get_system_status():
    """
    Get current system resource usage and status.
    
    Returns:
        SystemStatus with CPU, memory, disk metrics and overall status
    """
    # TODO: Call check_system_health() from policies
    # TODO: Build and return SystemStatus model
    pass

@app.post("/policy/check", response_model=PolicyCheckResponse)
async def check_policy(policy_request: PolicyCheckRequest):
    """
    Check if a request complies with defined policies.
    
    Args:
        policy_request: PolicyCheckRequest with request details
    
    Returns:
        PolicyCheckResponse indicating if request is allowed
    """
    # TODO: Validate request size using validate_request_size()
    # TODO: Validate HTTP method using validate_http_method()
    # TODO: Check rate limit using enforce_rate_limit()
    # TODO: Return PolicyCheckResponse with results
    pass

@app.get("/policies")
async def list_policies():
    """List all active policy rules"""
    # TODO: Return POLICY_RULES from config
    pass

@app.get("/limits")
async def get_resource_limits():
    """Get configured resource limit thresholds"""
    # TODO: Return RESOURCE_LIMITS from config
    pass

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware to log all incoming requests.
    """
    # TODO: Log request method and path
    # TODO: Call next middleware/endpoint
    # TODO: Log response status code
    # TODO: Return response
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
