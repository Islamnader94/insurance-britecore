import unittest
import json
import simplejson
import os
from app import app, db



class TestAPI(unittest.TestCase):

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True
        db.create_all()

    def tearDown(self):

        db.session.close()
        db.drop_all()



    def test_is_main_routing_working(self):
        """
        Test if the main route is answering with the correct status code.
        """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_get_fields(self):
        data = dict(name='test', number='83838', date='2018-08-15')
        response = self.client.post('/add', data=json.dumps(data), content_type='application/json')

        response = self.client.get('/add')

        assert response.status_code == 200


        assert field.get('name') == 'test'
        assert field.get('number') == '83838'
        assert field.get('date') == '2018-08-15'



if __name__ == '__main__':
    unittest.main()
