# Movies Manager App
This is a Django web application that allows you to manage and view a collection of movies.

## Requirements
* Python 3.x
* Django 3.x

## Features
* Display a list of all movies.
* Display details of a movie.
* Add a new movie.
* Delete a movie.

## Installation
1. Clone the repository <br>
``` git clone https://github.com/UsmanRepos/django-rest-frame-work-school-app.git ``` <br><br>
2. Install the required packages <br>
``` pip install -r requirements.txt ``` <br><br>
3. Run migrations <br>
``` python manage.py migrate ``` <br><br>
4. Run the development server  
``` python manage.py runserver ``` <br><br>

## Models
The Movie model has the following fields:
* title: a CharField with a maximum length of 120 characters.
* description: a CharField with a maximum length of 500 characters.
* year: an IntegerField for the year the movie was released.

## Views
The project includes the following views:
* movies: displays a list of all movies.
* details: displays details of a single movie with a given id.
* add: adds a new movie with given title, year, and description.
* delete: deletes a movie with a given id.

## Templates
The project includes the following templates:
* movies/movies.html: template for displaying a list of all movies.
* movies/details.html: template for displaying details of a single movie.
* movies/add.html: template for adding a new movie.

## Contributing
Contributions are welcome! If you would like to contribute to this project, you can start by forking the repository



