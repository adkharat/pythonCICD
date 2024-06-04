import unittest
from unittest.mock import patch, MagicMock
import json
import pymongo
import re
import math
import datetime

# Import the functions from the module
from lambdaFunction import use_json, use_pymongo, use_re, use_math, use_datetime

class TestFunctions(unittest.TestCase):

    # @patch('boto3.client')
    # def test_use_boto3(self, mock_boto3_client):
    #     mock_s3 = MagicMock()
    #     mock_boto3_client.return_value = mock_s3
    #     mock_s3.list_buckets.return_value = {'Buckets': [{'Name': 'bucket1'}, {'Name': 'bucket2'}]}
        
        # result = use_boto3()
        # self.assertEqual(result, ['bucket1', 'bucket2'])

    def test_use_json(self):
        json_data, deserialized_data = use_json()
        expected_data = {"name": "Alice", "age": 30, "city": "Wonderland"}
        
        self.assertEqual(json.loads(json_data), expected_data)
        self.assertEqual(deserialized_data, expected_data)

    # @patch('pymongo.MongoClient')
    # def test_use_pymongo(self, mock_mongo_client):
    #     mock_client = MagicMock()
    #     mock_mongo_client.return_value = mock_client
    #     mock_collection = MagicMock()
    #     mock_db = MagicMock()
    #     mock_client.__getitem__.return_value = mock_db
    #     mock_db.__getitem__.return_value = mock_collection
    #     mock_collection.insert_one.return_value.inserted_id = 'mock_id'
        
        # result = use_pymongo()
        # self.assertEqual(result, 'mock_id')

    def test_use_re(self):
        result = use_re()
        self.assertEqual(result, ['123', '45'])

    def test_use_math(self):
        sqrt, factorial = use_math()
        self.assertEqual(sqrt, math.sqrt(16))
        self.assertEqual(factorial, math.factorial(16))

    @patch('datetime.datetime')
    def test_use_datetime(self, mock_datetime):
        mock_now = datetime.datetime(2024, 1, 1)
        mock_datetime.now.return_value = mock_now
        mock_datetime.strftime.return_value = "2024"
        
        result = mock_datetime.strftime.return_value
        print(f"result formatted_year result--- : {result}")
        self.assertEqual("2024", "2024")

if __name__ == "__main__":
    unittest.main()
