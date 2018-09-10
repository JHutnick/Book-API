from flask import json, jsonify

from main import app
import unittest


# the tested class
class TestBooks(unittest.TestCase):

    # sets up Flask client
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_get_books(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/books/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

        # must start with test or wont run

    def test_put_books(self):
        # sends HTTP GET request to the application
        # on the specified path
        book = {"author": "Bob Smith",
                "genre": "Non Fiction",
                "bookname": "Flowers",
                "publishedDate": "Wed, 06 Dec 1995 00:00:00 GMT",
                "loanstatus": False
                }
        book = json.dumps(book)
        result = self.app.post('/books/',
                               content_type='application/json',
                               data=book)

        self.assertEqual(result.status_code, 200)

    def test_get_books_author(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/books/author/yudong book')

        # assert the response data
        self.assertEqual(result.status_code, 200)

    def test_get_books_genre(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/books/genre/action')

        # assert the response data
        self.assertEqual(result.status_code, 200)

    def test_new_loan(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.put('/books/1/loaned/1')

        # assert the response data
        self.assertEqual(result.status_code, 200)


# runs all the tests
if __name__ == '__main__':
    unittest.main()
