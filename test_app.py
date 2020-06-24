import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

casting_assit_token = "Bearer {}".format(os.environ.get('CAST_ASSIT_TOKEN'))
casting_direct_token = "Bearer {}".format(os.getenv('CAST_DIRECT_TOKEN'))
executive_prod_token = "Bearer {}".format(os.getenv('EXEC_PROD_TOKEN'))

class CastingAgencyUnitTest(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.getenv('DATABASETEST_URL')
        

        self.new_movie = {
            'title': 'New Movie',
            'release_date': '2025-01-08 04:05:06'
        }

        self.new_actor = {
            'name': 'New Actor',
            'age': 100,
            'gender': 'Female'
        }

        self.update_movie = {
            'title': 'Update Movie',
            'release_date': '2025-01-08 04:05:06'
        }

        self.update_actor = {
            'name': 'Update Actor',
            'age': 50,
            'gender': 'Female'
        }

        # Tokens to headers
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    # Successful Test Cases
    # ----------------------------------
    def test_get_movies(self):
        response = self.client().get('/movies', headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    
    def test_get_actors(self):
        response = self.client().get('/actors', headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['actors'])
    
    def test_post_movie(self):
        response = self.client().post('/movies', json=self.new_movie, headers={"Authorization": (executive_prod_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], "Movie Added Successfully")
    
    def test_post_actor(self):
        response = self.client().post('/actors', json=self.new_actor, headers={"Authorization": (casting_direct_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], "Actor Added Successfully")
    
    def test_patch_movie(self):
        response = self.client().patch('/movies/1', json=self.update_movie, headers={"Authorization": (casting_direct_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], "Movie Successfully Updated")

    def test_patch_actor(self):
        response = self.client().patch('/actors/1', json=self.update_actor, headers={"Authorization": (casting_direct_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], "Actor Successfully Updated")
    
    def test_delete_movie(self):
        response = self.client().delete('/movies/2', headers={"Authorization": (casting_direct_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
    
    def test_delete_actor(self):
        response = self.client().delete('/actors/2', headers={"Authorization": (casting_direct_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    # Error Behaviour Testcases
    #------------------------------

    def test_401_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
    
    def test_401_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
    
    #Error test cases for post request results in 401
    def test_401_create_movies(self):
        response = self.client().post('/movies', headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
    
    def test_401_create_actor(self):
        response = self.client().post('/actors', headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
    
    # If patch request receives an id that does not exists
    def test_404_update_movies(self):
        response = self.client().patch('/movies/100', json=self.update_movie, headers={"Authorization": (casting_direct_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)

    def test_404_update_actors(self):
        response = self.client().patch('/actors/100', json=self.update_actor, headers={"Authorization": (casting_direct_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
    
    # Error cases for bad permissions
    def test_401_update_movies(self):
        response = self.client().patch('/movies/1', json=self.update_movie, headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)

    def test_401_update_actors(self):
        response = self.client().patch('/actors/1', json=self.update_actor, headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
    
    # Error test cases for delete id that does not exists
    def test_404_delete_movies(self):
        response = self.client().delete('/movies/100', headers={"Authorization": (executive_prod_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)

    def test_404_delete_actors(self):
        response = self.client().delete('/actors/100', headers={"Authorization": (executive_prod_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)

    # Error test cases for bad persmission to delete
    def test_401_delete_movies(self):
        response = self.client().delete('/movies/3', headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)

    def test_401_delete_actors(self):
        response = self.client().delete('/actors/3', headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)

    # Error test cases for id not found
    def test_404_get_movies(self):
        response = self.client().get('/movies/100', headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)

    def test_404_get_actors(self):
        response = self.client().get('/actors/100', headers={"Authorization": (casting_assit_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
