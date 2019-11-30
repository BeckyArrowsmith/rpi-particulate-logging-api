from app import app, create_log
import json
import os
import requests
import unittest 
from unittest.mock import patch


class TestSomething(unittest.TestCase): 
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 
        

    def test_root_status_code(self):
        result = self.app.get('/') 

        self.assertEqual(result.status_code, 200) 
        self.assertEqual(result.data, b'Nothing to see here.')

    @patch('requests.post')
    def test_post(self, mock_post):
        payload = {"test1": "value1", "test2": "value2"}
        response = requests.post("http://www.someurl.com", data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        mock_post.assert_called_with("http://www.someurl.com", data=json.dumps(payload), headers={'Content-Type': 'application/json'})

if __name__ == '__main__':
    unittest.main()