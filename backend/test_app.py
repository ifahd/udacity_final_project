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
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            'postgres', 'root', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # token
        self.PRODUCER = os.environ.get('ASSISTANT')

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    # Test Create Movies
    # -------------------------------------------
    def test_post_movie(self):
        res = self.client().post(
            '/movies',
            json={
                "title": "The Shawshank Redemption",
                "release_date": "03/03/2020"},
            headers={
                'Authorization': "Bearer {}".format(
                    self.PRODUCER)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    # Test Update Movies By ID
    # -------------------------------------------
    def test_update_movie(self):
        res = self.client().patch('/movies/1', json={
            "title": "The Shawshank Redemption",
            "release_date": "01/01/2020"
        },
            headers={
            'Authorization': "Bearer {}".format(self.PRODUCER)
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    # Test GET All Movies
    # -------------------------------------------
    def test_get_movies(self):
        res = self.client().get(
            '/movies',
            headers={
                'Authorization': "Bearer {}".format(
                    self.PRODUCER)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # Test GET All Movies By ID
    # -------------------------------------------
    def test_get_movie(self):
        res = self.client().get(
            '/movies/1',
            headers={
                'Authorization': "Bearer {}".format(
                    self.PRODUCER)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Test Permissions
    # ---------------------------------------------------
    def test_permissions_get_movie(self):
        res = self.client().get('/movies/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Test 401 When not authentication
    # ---------------------------------------------------
    def test_401_get_movie(self):
        res = self.client().get('/movies/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()
