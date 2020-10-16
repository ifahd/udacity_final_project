import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Movie, Actor

class FinalAppTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "final_app_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('postgres', 'root', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    def tearDown(self):
        pass

    # Test Index
    #-------------------------------------------
    def test_index(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertTrue(data['message'])

    #-------------------------------------------
    # Test Movies
    #-------------------------------------------

    # Test Create Movies
    #-------------------------------------------
    def test_post_movie(self):
        res = self.client().post('/movies', json={
            "title": "Mr.Robot",
            "release_date": "03/03/2020"            
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Test Update Movies By ID
    #-------------------------------------------
    def test_update_movie(self):
        res = self.client().patch('/movies/1', json={
            "title": "Mr.Robot",
            "release_date": "03/03/2020"            
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Test GET All Movies
    #-------------------------------------------
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # Test GET All Movies By ID
    #-------------------------------------------
    def test_get_movie(self):
        res = self.client().get('/movies/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Test 401 When not authentication
    #---------------------------------------------------
    def test_401_get_movie(self):
        res = self.client().get('/movies/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    
if __name__ == "__main__":
    unittest.main()