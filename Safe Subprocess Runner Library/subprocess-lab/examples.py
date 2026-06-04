#!/usr/bin/env python3
from safe_runner import SafeSubprocessRunner

def example_system_info():
    """Gather system information safely."""
    runner = SafeSubprocessRunner(timeout=10)
    
    # TODO: Implement system info gathering
    # 1. Get current user
    # 2. Get current directory
    # 3. Get disk usage
    # 4. Display results in formatted way
    pass

def example_file_operations():
    """Perform safe file operations."""
    runner = SafeSubprocessRunner(timeout=10)
    
    # TODO: Implement file operations
    # 1. List files in current directory
    # 2. Count lines in a file
    # 3. Search for pattern in file
    pass

if __name__ == "__main__":
    print("=== System Information ===")
    example_system_info()
    
    print("\n=== File Operations ===")
    example_file_operations()
