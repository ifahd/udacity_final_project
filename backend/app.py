import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth, get_token_auth_header, verify_decode_jwt

def create_app(test_config=None):
  
  # configration
  # ------------------------------------------------------
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
      response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
      return response

  # ------------------------------------------------------
  # Endpoints
  # ------------------------------------------------------

  # Index 
  # ------------------------------------------------------
  @app.route('/')
  def index():
    # token = request.args.get('access_token')
    message = 'Welcome To Index' 
    # if not token:
    #   message += ' Your Token is:' + token 
    # access_token
    return jsonify({
      'message': message,
      'token': request.authorization
    })

  # Get Permission
  # ------------------------------------------------------
  @app.route('/permissions')
  def get_permissions():
    token = get_token_auth_header()
    permissions = verify_decode_jwt(token)
    # permissions = get_permissions()
    return jsonify({
      'permissions': permissions['permissions'],
      # 'token': token,
      # 'token': request.authorization
    })
  # ------------------------------------------------------
  # Movies
  # ------------------------------------------------------

  # GET All Movies 
  # ------------------------------------------------------
  @app.route('/movies')
  def get_movies():
    movies = Movie.query.all()

    return jsonify({
      'success': True,
      'movies': [movie.format() for movie in movies]
    }), 200

  # GET Movie By ID
  # ------------------------------------------------------
  @app.route('/movies/<int:id>', methods=['GET'])
  def get_movie(id):

    movie = Movie.query.get(id)

    if movie is None:
        abort(404)

    return jsonify({
        'movie': movie.format(),
        'success': True
    }), 200

  # POST New Movie
  # ------------------------------------------------------
  @app.route('/movies', methods=['POST'])
  def post_movie():

    title = request.get_json()['title']
    release_date = request.get_json()['release_date']

    movie = Movie(title=title, release_date=release_date)
    
    movie.insert()

    return jsonify({ 
        'movie': movie.format(),
        'success': True
    }), 200

  # PATCH Movie By ID
  # ------------------------------------------------------
  @app.route('/movies/<int:id>', methods=['PATCH'])
  def update_movie(id):

    movie = Movie.query.get(id)

    if movie is None:
        abort(404)

    if 'title' in request.get_json().keys() :
      movie.title = request.get_json()['title'] 

    if 'release_date' in request.get_json().keys() :
      movie.release_date = request.get_json()['release_date']          
    
    movie.update()

    return jsonify({
        'movie': movie.format(),
        'success': True
    }), 200

  # DELETE Movie By ID
  # ------------------------------------------------------
  @app.route('/movies/<int:id>', methods=['DELETE'])
  def delete_movie(id):
      
    movie = Movie.query.get(id)

    if movie is None:
      abort(404)

    try:
      movie.delete()
    except: 
      abort(400)

    return jsonify({
        'deleted': id,
        'success': True
    }), 200

  # ------------------------------------------------------
  # Actors
  # ------------------------------------------------------

  # GET All Actors 
  # ------------------------------------------------------
  @app.route('/actors')
  def get_actors():
    actors = Actor.query.all()

    return jsonify({
      'success': True,
      'actors': [actor.format() for actor in actors]
    }), 200

  # GET Actor By ID
  # ------------------------------------------------------
  @app.route('/actors/<int:id>', methods=['GET'])
  def get_actor(id):

    actor = Actor.query.get(id)

    if actor is None:
      abort(404)

    return jsonify({
        'actor': actor.format(),
        'success': True
    }), 200

  # POST New Actor
  # ------------------------------------------------------
  @app.route('/actors', methods=['POST'])
  def post_actor():

    name = request.get_json()['name']
    age = request.get_json()['age']
    gender = request.get_json()['gender']

    actor = Actor(
      name=name, 
      age=age,
      gender=gender,
    )
    
    actor.insert()

    return jsonify({ 
        'movie': actor.format(),
        'success': True
    }), 200

  # PATCH Actors By ID
  # ------------------------------------------------------
  @app.route('/actors/<int:id>', methods=['PATCH'])
  def update_actor(id):

    actor = Actor.query.get(id)

    if actor is None:
        abort(404)

    if 'name' in request.get_json().keys() :
      actor.name = request.get_json()['name'] 

    if 'age' in request.get_json().keys() :
      actor.age = request.get_json()['age']          

    if 'gender' in request.get_json().keys() :
      actor.gender = request.get_json()['gender']          
    
    actor.update()

    return jsonify({
        'actor': actor.format(),
        'success': True
    }), 200

  # DELETE Actors By ID
  # ------------------------------------------------------
  @app.route('/actors/<int:id>', methods=['DELETE'])
  def delete_actor(id):
      
    actor = Actor.query.get(id)

    if actor is None:
      abort(404)

    try:
      actor.delete()
    except: 
      abort(400)

    return jsonify({
        'deleted': id,
        'success': True
    }), 200

  # ------------------------------------------------------
  # Error Handler 
  # ------------------------------------------------------

  # Error 400 
  # ------------------------------------------------------
  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          'success': False,
          'error': 400,
          'message': 'Bad request',
      }), 400

  # Error 404 
  # ------------------------------------------------------
  @app.errorhandler(404)
  def resource_not_found(error):
      return jsonify({
          'success': False,
          'error': 404,
          'message': 'Resource not found',
      }), 404

  # Error 405 
  # ------------------------------------------------------
  @app.errorhandler(405)
  def method_not_allowed(error):
      return jsonify({
          'success': False,
          'error': 405,
          'message': 'Method not allowed',
      }), 405

  # Error 422 
  # ------------------------------------------------------
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          'success': False,
          'error': 422,
          'message': 'Unprocessable',
      }), 422

  # Error 500 
  # ------------------------------------------------------
  @app.errorhandler(500)
  def Internal_server_error(error):
      return jsonify({
          'success': False,
          'error': 500,
          'message': 'Internal server error',
      }), 500

  # Auth  Error 
  # ------------------------------------------------------

  @app.errorhandler(AuthError)
  def auth_error(error):
      return jsonify({
          'success': False,
          'error': error.status_code,
          'message': error.error['description'],
      }), error.status_code

  return app



APP = create_app()

if __name__ == '__main__':
  APP.run(host='0.0.0.0', port=8080, debug=True)