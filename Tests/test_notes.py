from flask import json

from main import app
import unittest


# the tested class
class TestNotes(unittest.TestCase):

    # sets up Flask client
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_add_bookNote(self):
        # sends HTTP GET request to the application
        # on the specified path
        note = {"text": "test"
                }
        note = json.dumps(note)
        result = self.app.post('/books/1/note/1',
                               content_type='application/json',
                               data=note)

        # assert the response data
        self.assertEqual(result.status_code, 200)

    def test_delete_bookNote(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.delete('/books/1/note/1')

        # assert the response data
        self.assertEqual(result.status_code, 200)

# runs all the tests
if __name__ == '__main__':
    unittest.main()