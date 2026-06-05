from resilient_client import ResilientHTTPClient
import time

client = ResilientHTTPClient(max_retries=3, base_timeout=2)

# Test 1: Verify backoff calculation
print("Backoff delays:")
for i in range(4):
    delay = client._calculate_backoff(i)
    print(f"  Attempt {i}: {delay}s")

# Test 2: Verify successful request
try:
    response = client.get("https://httpbin.org/status/200")
    print(f"\nSuccess test: Status {response.status_code}")
except Exception as e:
    print(f"Failed: {e}")

client.close()
