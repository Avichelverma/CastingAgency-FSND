# CASTING AGENCY API ENDPOINTS (CAPSTONE PROJECT)

Casting Agency API models a company that is responsible for creating movies and managing and assigning actors to those movies. This API endpoints helps in simplifying and streamlining the backend process.

The API is responsible for handling CRUD operations and checks for authorization before commiting anything to database.

This is a Capstone Project for Full-Stack Nanodegree at Udacity.

The API is hosted on heroku at
```
https://castingworld.herokuapp.com/
```

## Getting Started

Created REST APIs for Casting Agency.
The Technologies used in the stack are as followings:

- Python 3.7
- Flask
- SQLAlchemy ORM
- Postgres SQL
- Auth0.com (Authentication purpose)

### Installing Dependencies
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the `/` directory and running:
```bash

pip install -r requirements.txt

```
This will install all of the required packages we selected within the `requirements.txt` file.

### Database Setup
Restore a database using the castingagency.sql. It is present in the root folder of the project.

You can restore the database using command
```
pg_restore -U postgres -d castingagency < castingagency.sql
```
Create a test database using the same command
```
pg_restore -U postgres -d castingagency_test < castingagency.sql
```

### Key Dependencies

-  [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

-  [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

-  [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.
- 
## Running the Server

First you need to setup the environment variable. You can copy and input the variable from the setup.sh file.

To run a flask server:
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
## Unit Testing the API Endpoints

To run the tests, navigate to root folder and first drop the database if created and then create test database again

Once database is all setup.

Run python test script command
```
python test_app.py
```
## Brief Info regarding Roles and Permissions
- Models:
- - Movies with attributes title and release date
- - Actors with attributes name, age and gender
- Endpoints:
- - GET /actors and /movies
- - DELETE /actors/ and /movies/
- - POST /actors and /movies and
- - PATCH /actors/ and /movies/
- Roles:
- - Casting Assistant
- - - Can view actors and movies
- - Casting Director
- - - All permissions a Casting Assistant has and…
- - - Add or delete an actor from the database
- - - Modify actors or movies
- - Executive Producer
- - - All permissions a Casting Director has and…
- - - Add or delete a movie from the database

## API Reference Guide

Sample Curl request 
```
curl -H "Authorization: Bearer $TOKEN" -X GET castingworld.herokuapp.com/movies
```

### Error Handling
- 200 - Success Code
- Following errors are handled with their status codes:
- 400 - Bad Error Request
- 401 - Authorization Header is expected
- 403 - Payload does not contain persmissions
- 404 - Resource Not Found
- 405 - Method not allowed
- 422 - Unproccessable Request
- 500 - Internal Server Error
- Errors are returned in json format.

```
{
	'success': False,
	'error': 422,
	'message': 'Unproccessable Request'
}
```
### API Endpoints Documentations

#### GET/movies
- Returns list of movies with id, title and release_date.
- Sample endpoint command : ```castingworld.herokuapp.com/movies```
 Sample Output
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 08 Jan 2016 04:05:06 GMT",
            "title": "Iron Man 2"
        },
        {
            "id": 2,
            "release_date": "Sun, 08 Jan 2017 04:05:06 GMT",
            "title": "Iron Man 3"
        },
        {
            "id": 3,
            "release_date": "Sun, 08 Jan 2017 04:05:06 GMT",
            "title": "Iron Man 3"
        },
        {
            "id": 4,
            "release_date": "Sun, 08 Jan 2017 04:05:06 GMT",
            "title": "Iron Man 3"
        }
    ],
    "success": true,
    "total_movies": 4
}
```
#### GET/actors
- Returns a list of actors with name, age, gender
- Sample endpoint command : ```castingworld.herokuapp.com/actors```
Sample Output
```
{
    "actors": [
        {
            "age": 36,
            "gender": "Male",
            "id": 1,
            "name": "Chris Hemsworth"
        },
        {
            "age": 24,
            "gender": "Female",
            "id": 2,
            "name": "Emma Stone"
        }
    ],
    "success": true,
    "total_actors": 2
}
```
#### GET/movies/1
- Returns a movie with id, title and release_date.
Sample Output
```
{
    "movie": {
        "id": 2,
        "release_date": "Sun, 08 Jan 2017 04:05:06 GMT",
        "title": "Iron Man 3"
    },
    "success":
```
#### GET/actors/2
- Returns an actor with name, age, gender
Sample Output
```
{
    "actor": {
        "age": 24,
        "gender": "Female",
        "id": 2,
        "name": "Emma Stone"
    },
    "success": true
}
```
#### POST/movies
- Post a new movie to movie table
- Request Body : {title: string, release_date:string}
- Returns a successful message with new movie_id
Sample Output
```
{
    "actors": [
        {
            "age": 36,
            "gender": "Male",
            "id": 1,
            "name": "Chris Hemsworth"
        },
        {
            "age": 24,
            "gender": "Female",
            "id": 2,
            "name": "Emma Stone"
        }
    ],
    "success": true,
    "total_actors": 2
}
```

#### POST/actors
- Post a new actor to the actor table
- Request Body : {name: string, age:integer, gender:string}
- Return a successful message with new actor_id
Sample Output
```
{
    "actor": {
        "age": 36,
        "gender": "Male",
        "id": 1,
        "name": "Chris Hemsworth"
    },
    "message": "Actor Added Successfully",
    "success": true
}
```

#### PATCH/movies/1
- Takes movie_id as params and update the particular id with title and release_date
- Request Body : {title: string, release_date:string}
- Returns a successful message with movie_id
Sample Output
```
{
    "message": "Movie Successfully Updated",
    "movie_id": 1,
    "success": true
}
```


#### PATCH/actors/1
- Takes actor_id as params and update the particular id with name, age, gender
- Request Body : {title: string, release_date:string}
- Returns a successful message with actor_id
Sample Output
```
{
    "actor_id": 1,
    "message": "Actor Successfully Updated",
    "success": true
}
```

#### DELETE/movies/1
- Takes movie_id and delete the particular entry from table
- Returns a successful message with movie_id
Sample Output
```
{
    "deleted movie_id": 1,
    "success": true
}
```
#### DELETE/actors/1
- Takes actor_id and delete the particular entry from table
- Returns a successful message with actor_id
Sample Output
```
{
    "deleted actor_id": 1,
    "success": true
}
```

### Author
- Avichel Verma developed the following APIs; Successfully tested the APIs using unittests
- Udacity for offering me a chance to work on this degree