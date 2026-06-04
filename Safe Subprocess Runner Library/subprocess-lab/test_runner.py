#!/usr/bin/env python3
from safe_runner import SafeSubprocessRunner

def test_basic_execution():
    """Test basic command execution."""
    runner = SafeSubprocessRunner(timeout=10)
    
    # TODO: Test valid commands
    # Test 1: Execute 'ls -la'
    # Test 2: Execute 'echo "Hello World"'
    # Test 3: Execute 'pwd'
    
    print("Basic execution tests:")
    # Implement your tests here
    pass

def test_validation():
    """Test input validation and security."""
    runner = SafeSubprocessRunner(timeout=10)
    
    # TODO: Test invalid commands
    # Test 1: Try command injection with '; rm -rf /'
    # Test 2: Try piping with '|'
    # Test 3: Try command not in whitelist
    
    print("\nValidation tests:")
    # Implement your tests here
    pass

def test_timeout():
    """Test timeout handling."""
    runner = SafeSubprocessRunner(timeout=2)
    
    # TODO: Test timeout
    # Test: Execute 'sleep 5' with 2-second timeout
    
    print("\nTimeout tests:")
    # Implement your tests here
    pass

def test_error_handling():
    """Test error handling."""
    runner = SafeSubprocessRunner(timeout=10)
    
    # TODO: Test error scenarios
    # Test 1: Non-existent file with 'cat'
    # Test 2: Invalid arguments
    
    print("\nError handling tests:")
    # Implement your tests here
    pass

if __name__ == "__main__":
    test_basic_execution()
    test_validation()
    test_timeout()
    test_error_handling()
