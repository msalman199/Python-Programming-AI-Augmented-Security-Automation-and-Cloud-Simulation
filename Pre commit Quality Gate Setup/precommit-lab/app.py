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
