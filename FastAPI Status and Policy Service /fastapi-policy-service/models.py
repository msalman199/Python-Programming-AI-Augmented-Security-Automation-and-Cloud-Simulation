from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

class SystemStatus(BaseModel):
    """Model for system status response"""
    timestamp: datetime
    cpu_percent: float
    memory_percent: float
    disk_percent: float
    status: str  # "healthy", "warning", "critical"

class PolicyCheckRequest(BaseModel):
    """Model for policy check requests"""
    # TODO: Add fields for request_size, method, user_id
    pass

class PolicyCheckResponse(BaseModel):
    """Model for policy check responses"""
    # TODO: Add fields for allowed (bool), reason (str), policy_name (str)
    pass

class HealthResponse(BaseModel):
    """Model for health check response"""
    status: str
    timestamp: datetime
    service: str = "FastAPI Policy Service"
