import boto3
import json
import pymongo
import re
import math
import datetime
# json, re, math, and datetime are standard Python modules that come with the Python standard library, so they do not need to be installed.

# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main program
if __name__ == "__main__":
    # Get input from the user
    # num1 = float(input("Enter the first number: "))
    # num2 = float(input("Enter the second number: "))

    # Calculate the sum
    result = add_numbers(2, 3)

    # Print the result
    print(f"The sum of 2 and 3 is {result}")
