from typing import Dict, Tuple
from config import RESOURCE_LIMITS, POLICY_RULES
import psutil

def check_system_health() -> Tuple[str, Dict[str, float]]:
    """
    Check system resource usage and determine health status.
    
    Returns:
        Tuple of (status_string, metrics_dict)
        status can be: "healthy", "warning", "critical"
    """
    # TODO: Get CPU, memory, and disk usage using psutil
    # TODO: Compare against RESOURCE_LIMITS
    # TODO: Return appropriate status and metrics
    pass

def validate_request_size(size_bytes: int) -> Tuple[bool, str]:
    """
    Validate if request size is within policy limits.
    
    Args:
        size_bytes: Size of the request in bytes
    
    Returns:
        Tuple of (is_valid, reason_message)
    """
    # TODO: Check against POLICY_RULES["max_request_size"]
    # TODO: Return validation result and appropriate message
    pass

def validate_http_method(method: str) -> Tuple[bool, str]:
    """
    Validate if HTTP method is allowed by policy.
    
    Args:
        method: HTTP method string (GET, POST, etc.)
    
    Returns:
        Tuple of (is_valid, reason_message)
    """
    # TODO: Check if method is in POLICY_RULES["allowed_methods"]
    # TODO: Return validation result and message
    pass

def enforce_rate_limit(user_id: str, request_count: int) -> Tuple[bool, str]:
    """
    Check if user has exceeded rate limit.
    
    Args:
        user_id: Identifier for the user
        request_count: Number of requests in current window
    
    Returns:
        Tuple of (is_allowed, reason_message)
    """
    # TODO: Compare request_count against POLICY_RULES["rate_limit_per_minute"]
    # TODO: Return whether request is allowed
    pass
