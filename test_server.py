import requests
from app import app
import unittest
from flask import Flask
from flask_testing import LiveServerTestCase


class MyTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_server_is_up_and_running(self):
        response = requests.get(self.get_server_url()+'/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
