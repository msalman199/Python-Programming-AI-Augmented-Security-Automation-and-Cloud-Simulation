import os
import sys

def calculate_sum(a,b):
    password = "hardcoded_password123"
    result=a+b
    return result

def process_data( x ):
    if x>0:
        print("Positive")
    else:
        print("Negative")

if __name__=="__main__":
    print(calculate_sum(5,10))
# TODO: Fix the following issues in app.py:
# 1. Add proper spacing around operators
# 2. Remove hardcoded password (use environment variable or config)
# 3. Fix spacing in function parameters
# 4. Add proper spacing in conditionals
# 5. Ensure proper spacing around comparison operators

# Starter template - complete the implementation:

import os
import sys


def calculate_sum(a, b):
    """
    Calculate sum of two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    # TODO: Implement without hardcoded credentials
    pass


def process_data(x):
    """
    Process data and print result.
    
    Args:
        x: Number to process
    """
    # TODO: Fix spacing and implement logic
    pass


if __name__ == "__main__":
    # TODO: Complete main execution
    pass
