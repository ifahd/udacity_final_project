# FSND - Capstone (Udacity Final Project)
---
### Live URL `Hosted on Heroku`
**Frontend**
```
https://final-project-fahd.herokuapp.com
```
**Backend** 
```
https://api-final-project-fahd.herokuapp.com
```
# Motivation
---
This is my Final Project for Udacity FSND `Full-Stack Developer Nanodegree program`
The project is to test my ability to:
- Build Data Modeling.
- API Architecture and Testing.
- Use Third-Party Authentication `Auth0`.
- Deployment on `Heroku`.
- Code Quality & Documentation using `PEP 8 style`.
# frontend
---
## Build Setup

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

# Backend `API`
---
## Getting Started
### Installing Dependencies
#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server
From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
## Authentication
###### The app use Auth0 for Authentication:
The app has three **Roles**:
- **Casting Assistant**:
Can view actors and movies.
**Permissions:**
`read:actors` `read:movies`
- **Casting Director**:
All permissions a Casting Assistant has and Add an actor from the database Modify actors or movies.
**Permissions:**
`read:actors` `read:movies` `create:actors` `create:movies` `update:actors` `update:movies`

- **Executive Producer**: 
All permissions a Casting Director has and delete a movie from the database.
**Permissions:**
`read:actors` `read:movies` `create:actors` `create:movies` `update:actors` `update:movies` `delete:actors` `delete:movies`

## For Testing:
Use this URL `(Hosted on Heroku)`
```
https://final-project-fahd.herokuapp.com
```
to login with any account below after login you can get token in index page and copy token and test endpoints.
### Accounts for test:
- casting.assistant@test.com **(Casting Assistant)**
- casting.director@test.com **(Casting Director)**
- executive.producer@test.com **(Executive Producer)**

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Resource Not Found"
}
```
The API will return Many types when requests fail:
- 400: Bad request
- 404: Resource Not Found
- 405: Method not allowed
- 422: Unprocessable 
- 500: Internal server error 
- And Auth Error like (301, 401, ....)

### Endpoints 
#### Movies
---
#### GET /movies
- Fetches a dictionary of movies.
- Request Arguments: None
- Returns: An object with movies array, success Boolean. 
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Tue, 03 Mar 2020 00:00:00 GMT",
            "title": "The Shawshank Redemption"
        }
    ],
    "success": true
}
```
#### GET /movies/1
- Fetches a object of movies by id.
- Request Arguments: id
- Returns: An object with movie object, success Boolean. 
```
{
    "movie": {
        "id": 1,
        "release_date": "Tue, 03 Mar 2020 00:00:00 GMT",
        "title": "The Shawshank Redemption"
    },
    "success": true
}
```
#### POST /movies
- Create new movies.
- Request Arguments: title `(String)` , release_date `(String)`
- Returns: An object with movie object, success Boolean. 
```
{
    "movie": {
        "id": 1,
        "release_date": "Tue, 03 Mar 2020 00:00:00 GMT",
        "title": "The Shawshank Redemption"
    },
    "success": true
}
```
#### PATCH /movies/1
- Update movies by id.
- Request Arguments: title `(String)` | release_date `(String)`
- Returns: An object with movie object, success Boolean. 
```
{
    "movie": {
        "id": 1,
        "release_date": "Tue, 03 Mar 2020 00:00:00 GMT",
        "title": "The Shawshank Redemption"
    },
    "success": true
}
```
#### DELETE /movies/1
- Delete movies by id.
- Request Arguments: id `(Int)`
- Returns: An object with deleted key with id, success Boolean. 
```
{
    "deleted": 1,
    "success": true
}
```
#### Actors
---
#### GET /actors
- Fetches a dictionary of actors.
- Request Arguments: None
- Returns: An object with actors array, success Boolean. 
```
{
    "actors": [
        {
            "age": 33,
            "gender": "Male",
            "id": 1,
            "name": "Fahd"
        }
    ],
    "success": true
}
```
#### GET /actors/1
- Fetches a object of actors by id.
- Request Arguments: id
- Returns: An object with actor object, success Boolean. 
```
{
    "actor": {
        "age": 33,
        "gender": "Male",
        "id": 1,
        "name": "Fahd"
    },
    "success": true
}
```
#### POST /actors
- Create new actors.
- Request Arguments: name `(String)` , age `(Int)`, gender `(String)`
- Returns: An object with actor object, success Boolean. 
```
{
    "actor": {
        "age": 33,
        "gender": "Male",
        "id": 1,
        "name": "Fahd"
    },
    "success": true
}
```
#### PATCH /actors/1
- Update actors by id.
- Request Arguments: name `(String)` | age `(Int)` | gender `(String)`
- Returns: An object with actor object, success Boolean. 
```
{
    "actor": {
        "age": 33,
        "gender": "Male",
        "id": 1,
        "name": "Fahd"
    },
    "success": true
}
```
#### DELETE /actors/1
- Delete actors by id.
- Request Arguments: id `(Int)`
- Returns: An object with deleted key with id, success Boolean. 
```
{
    "deleted": 1,
    "success": true
}
```