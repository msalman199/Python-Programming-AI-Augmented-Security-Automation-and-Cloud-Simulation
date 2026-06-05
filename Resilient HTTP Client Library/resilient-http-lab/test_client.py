from resilient_client import ResilientHTTPClient
import json

def test_successful_request():
    """Test basic successful request."""
    print("\n=== Test 1: Successful Request ===")
    client = ResilientHTTPClient(max_retries=3, base_timeout=10)
    
    try:
        # TODO: Make a GET request to https://httpbin.org/get
        # Print status code and response JSON
        pass
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

def test_timeout_handling():
    """Test timeout with retry."""
    print("\n=== Test 2: Timeout Handling ===")
    # TODO: Create client with short timeout (1 second)
    # Try to request https://httpbin.org/delay/5
    # Observe retry behavior
    pass

def test_retry_on_failure():
    """Test retry on connection failure."""
    print("\n=== Test 3: Retry on Failure ===")
    # TODO: Create client
    # Try to request invalid URL: http://invalid-domain-12345.com
    # Observe retry attempts and backoff
    pass

def test_post_request():
    """Test POST request with data."""
    print("\n=== Test 4: POST Request ===")
    # TODO: Create client
    # POST to https://httpbin.org/post with JSON data
    # Print response
    pass

if __name__ == "__main__":
    test_successful_request()
    test_timeout_handling()
    test_retry_on_failure()
    test_post_request()
