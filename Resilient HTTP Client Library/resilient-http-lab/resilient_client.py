import requests
import time
from typing import Optional, Dict, Any
from requests.exceptions import RequestException, Timeout, ConnectionError

class ResilientHTTPClient:
    """
    A resilient HTTP client with retry logic, backoff, and timeout handling.
    """
    
    def __init__(
        self,
        max_retries: int = 3,
        base_timeout: int = 5,
        backoff_factor: float = 2.0
    ):
        """
        Initialize the resilient HTTP client.
        
        Args:
            max_retries: Maximum number of retry attempts
            base_timeout: Base timeout in seconds for requests
            backoff_factor: Multiplier for exponential backoff
        """
        self.max_retries = max_retries
        self.base_timeout = base_timeout
        self.backoff_factor = backoff_factor
        self.session = requests.Session()
    
    def _calculate_backoff(self, attempt: int) -> float:
        """
        Calculate exponential backoff delay.
        
        Args:
            attempt: Current retry attempt number (0-indexed)
        
        Returns:
            Delay in seconds
        
        TODO: Implement exponential backoff calculation
        Formula: base_delay * (backoff_factor ^ attempt)
        Use base_delay = 1 second
        """
        pass
    
    def _should_retry(self, exception: Exception, attempt: int) -> bool:
        """
        Determine if request should be retried based on exception type.
        
        Args:
            exception: The exception that occurred
            attempt: Current attempt number
        
        Returns:
            True if should retry, False otherwise
        
        TODO: Implement retry logic
        - Retry on Timeout, ConnectionError
        - Don't retry if max_retries exceeded
        - Don't retry on 4xx client errors (except 429)
        """
        pass
    
    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        """
        Perform a GET request with retry logic.
        
        Args:
            url: Target URL
            params: Query parameters
            headers: Request headers
        
        Returns:
            Response object
        
        Raises:
            RequestException: If all retries fail
        
        TODO: Implement the resilient GET request
        - Loop through retry attempts
        - Apply timeout
        - Catch exceptions and determine if retry needed
        - Apply backoff delay between retries
        - Log retry attempts (use print for simplicity)
        """
        pass
    
    def post(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        """
        Perform a POST request with retry logic.
        
        Args:
            url: Target URL
            data: Form data
            json: JSON payload
            headers: Request headers
        
        Returns:
            Response object
        
        TODO: Implement similar to GET but for POST requests
        Note: Be careful with retrying POST - consider idempotency
        """
        pass
    
    def close(self):
        """Close the session."""
        self.session.close()
resilient_client.py

