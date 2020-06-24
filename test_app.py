import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

assistant_token = "Bearer {}".format('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhzRVVvT0k3RTdZeFdCNE80Yk5zTyJ9.eyJpc3MiOiJodHRwczovL2Zuc2RsZWFybmluZy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmMTE3Zjk3ZmIzZjAwMDEzZTRkMTA4IiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU5Mjk2NzEwMiwiZXhwIjoxNTkyOTc0MzAyLCJhenAiOiJBc1p4Ym9ld2ZUeWlmOUtoNGlaRklYNVFCZWtyUmFJNiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.bLzL-JOKgtBz3YAO2KD2BGnzrLFo67kun7maQzgrFqTRCX9-fG7stAcxsPzc1aJQuJGr0U23a5go6W8iBf3TVeRfkgDesnyCe2c_o0I8yaG3KN3hm62WeVKmwf8ll3uaZwWIEHkgfk1qHyKTI4rzNIj19pZ0XUgkE90fV1b3Y9QI2H9a3eXNAYviBMz8obhspwDfSzFHvLuidpCKZh58EH5HQpP0LjWvT9Y8XJ7LJQz4QfeIOhapQYwC_2l8F0iMa-DQ0fvvUaI9MWKWwJ4g08CpbeH31enI-OCavZ2hAxl7WVWxVXN4jEtn-NRUWyVdM4YpzhqVNMxZpxZCx2SzqA')

class CastingAgencyUnitTest(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "castingagency_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'avi_1074', 'localhost:5432', self.database_name)

        # Tokens to headers
        self.casting_assistant = {'Authorization': 'Bearer {}'.format(
            'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhzRVVvT0k3RTdZeFdCNE80Yk5zTyJ9.eyJpc3MiOiJodHRwczovL2Zuc2RsZWFybmluZy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlZmJjZWQ1NWVlZjIwMDE5MmY0Yzc3IiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU5Mjk1NTAxNywiZXhwIjoxNTkyOTYyMjE3LCJhenAiOiJBc1p4Ym9ld2ZUeWlmOUtoNGlaRklYNVFCZWtyUmFJNiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.QN8kr6chQdWed95YTfSWWKDIg6b5kqqNKj1ZY1RRHD9Qlb6r7n1bGveML4KiTsMlcRpKtEKdHr7N5NxxyEgUQ-VjomOfYQZ_GMA594dxk0mFsHh9YUm04T4VyBs53ex5Xhck0GIPGdK4L5F_iHF0wojObAjEvBYMeqUaUavTOSIl7iC1x7utQSb8Z0EItfuhYd4pxzDSNNEX-Nhr3hz7XSEua8EYswxAQJIsI_LwGnF4gIBFB0duQkdFDmR5pKP5D5XRpYDD9yPjCv9oiCzQh3AM0pSAkiRkn0WwJPaZgQogUcyYuZE9inUg4AN2qlPJysj00EBo03H9_-yqeL03uQ')}

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_movies(self):
        print(self.casting_assistant)
        print("-----------------")
        response = self.client().get('/movies', headers={"Authorization": (assistant_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])


if __name__ == "__main__":
    unittest.main()
