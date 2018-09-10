from main import app
import unittest



# the tested class
class TestWorld(unittest.TestCase):

    # sets up Flask client
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

        # must start with test or wont run

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the response data
        self.assertEqual(result.data, b'Welcome to MSD Library Project')

# runs all the tests
if __name__ == '__main__':
    unittest.main()
