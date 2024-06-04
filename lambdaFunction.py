import boto3
import json
import pymongo
import re
import math
import datetime
# json, re, math, and datetime are standard Python modules that come with the Python standard library, so they do not need to be installed.

def use_json():
    # Example function that serializes and deserializes JSON
    data = {"name": "Alice", "age": 30, "city": "Wonderland"}
    json_data = json.dumps(data)
    print(f"JSON - Serialized Data: {json_data}")
    deserialized_data = json.loads(json_data)
    print(f"JSON - Deserialized Data: {deserialized_data}")
    return json_data, deserialized_data

def use_pymongo():
    # Example function that connects to a MongoDB database and inserts a document
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["testdb"]
        collection = db["testcollection"]
        document = {"name": "Bob", "age": 25, "city": "Builderland"}
        result = collection.insert_one(document)
        print(f"Pymongo - Inserted Document ID: {result.inserted_id}")
        return result.inserted_id
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print(f"Pymongo - Could not connect to MongoDB: {err}")

def use_re():
    # Example function that uses regex to find all numbers in a string
    text = "The price is 123 dollars and 45 cents"
    pattern = r'\d+'
    numbers = re.findall(pattern, text)
    print(f"re - Numbers in text: {numbers}")
    return numbers

def use_math():
    # Example function that calculates the square root and the factorial of a number
    number = 16
    sqrt_val = math.sqrt(number)
    factorial_val = math.factorial(number)
    print(f"math - Square Root of {number}: {sqrt_val}")
    print(f"math - Factorial of {number}: {factorial_val}")
    return sqrt_val, factorial_val

def use_datetime():
    # Example function that gets the current date and time and formats it
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"datetime - Current Date and Time: {formatted_date}")
    return formatted_date

if __name__ == "__main__":
    # use_boto3()
    use_json()
    # use_pymongo()
    use_re()
    use_math()
    use_datetime()
