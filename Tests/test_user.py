from main import app
import unittest

from flask import json, jsonify

# the tested class
class TestUsers(unittest.TestCase):

    # sets up Flask client
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_get_users(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/users/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    # must start with test or wont run

    def test_put_users(self):
        # sends HTTP GET request to the application
        # on the specified path
        user = {
            "email": "test@test.com",
            "isadmin": False,
            "firstname": "TestFirst",
            "lastname": "TestLast",
            "phone": "123456789"
        }
        user = json.dumps(user)

        result = self.app.post('/users/', content_type='application/json', data=user)

        self.assertEqual(result.status_code, 200)

    def test_delete_users(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.delete('/users/1')

        # assert the response data
        self.assertEqual(result.status_code, 200)


# runs all the tests
if __name__ == '__main__':
    unittest.main()
