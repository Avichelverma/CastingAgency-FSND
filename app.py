import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

from models import Actor, Movie, movie_list, setup_db
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    @app.route('/')
    def index():
        return("Casting Agency")

    @app.after_request
    def after_request(response):
        """ Set Access Control """

        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, PATCH, DELETE, OPTIONS')

        return response

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(token):
        movies = Movie.query.all()
        if(len(movies) == 0):
            abort(404)

        movies_format = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': movies_format,
            'total_movies': len(movies_format)
        }, 200)

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(token):
        actors = Actor.query.all()
        if(len(actors) == 0):
            abort(404)

        actors_format = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': actors_format,
            'total_actors': len(actors_format)
        }, 200)

    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:movies')
    def get_movie_id(token, movie_id):
        movie_detail = Movie.query.filter_by(id=movie_id).one_or_none()

        if(movie_detail is None):
            abort(404)

        return jsonify({
            'success': True,
            'movie': movie_detail.format()
        }, 200)

    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth('get:actors')
    def get_actor_id(token, actor_id):
        actor_detail = Actor.query.filter_by(id=actor_id).one_or_none()

        if(actor_detail is None):
            abort(404)

        return jsonify({
            'success': True,
            'actor': actor_detail.format()
        }, 200)

    # Delete methods
    # ---------------------------

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie_id(token, movie_id):
        movie_detail = Movie.query.filter_by(id=movie_id).one_or_none()

        if movie_detail is None:
            abort(404)

        movie_detail.delete()

        return jsonify({
            'success': True,
            'deleted movie_id': movie_id
        }, 200)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor_id(token, actor_id):
        actor_detail = Actor.query.filter_by(id=actor_id).one_or_none()

        if actor_detail is None:
            abort(404)

        actor_detail.delete()

        return jsonify({
            'success': True,
            'deleted actor_id': actor_id
        }, 200)

    # POST ENDPOINTS IMPLEMENTATION
    # ---------------------------------------

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(token):
        data = request.get_json()
        title = data.get('title', None)
        release_date = data.get('release_date', None)

        if title is None:
            abort(422)

        movie_list = Movie.query.filter(Movie.title == title).all()

        if (len(movie_list) > 0):
            abort(400)

        new_movie = Movie(title=title, release_date=release_date)

        new_movie.insert()

        return jsonify({
            'success': True,
            'message': "Movie Added Successfully",
            'movie': new_movie.format()
        }, 200)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(token):
        data = request.get_json()
        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)

        if name is None:
            abort(422)

        actor_list = Actor.query.filter(Actor.name == name).all()

        if (len(actor_list) > 0):
            abort(400)

        new_actor = Actor(name=name, age=age, gender=gender)

        new_actor.insert()

        return jsonify({
            'success': True,
            'message': "Actor Added Successfully",
            'actor': new_actor.format()
        }, 200)

    # PATCH ENDPOINT IMPLEMENTATION

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movie_id(token, movie_id):

        data = request.get_json()
        title = data.get('title', None)
        release_date = data.get('release_date', None)

        if(title is None or release_date is None):
            abort(422)

        movie_detail = Movie.query.filter(
            Movie.id == movie_id).one_or_none()

        if title:
            movie_detail.title = title
        if release_date:
            movie_detail.release_date = release_date

        movie_detail.update()

        return jsonify({
            "success": True,
            "message": "Movie Successfully Updated",
            "movie_id": movie_id
        }, 200)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actor_id(token, actor_id):

        data = request.get_json()
        print(data)
        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)

        if(name is None or age is None or gender is None):
            abort(422)

        actor_detail = Actor.query.filter(
            Actor.id == actor_id).one_or_none()

        if name:
            actor_detail.name = name
        if age:
            actor_detail.age = age
        if gender:
            actor_detail.gender = gender

        actor_detail.update()

        return jsonify({
            "success": True,
            "message": "Actor Successfully Updated",
            "actor_id": actor_id
        }, 200)

    # ERROR HANDLINGS

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "Bad Request"
        }, 400)

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': "Not Authorized"
        }, 401)

    @app.errorhandler(403)
    def bad_permission(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': "Bad Permission"
        }, 403)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Request Not Found"
        }, 404)

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': "Method not allowed"
        }, 405)

    @app.errorhandler(422)
    def unprocessable_request(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "Request cannot be processed"
        }, 422)

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': "Internal Server Error"
        }, 500)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
