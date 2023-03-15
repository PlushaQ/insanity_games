# Insanity Games - Website for Non-Existing Insanity Games Studio
#### Video Demo:  https://youtu.be/z15iDoI4clQ
#### Description:
This website is a web-based platform for non-existing Insanity Games studio. This website is created purely for fun and imagination, and does not intend to infringe on any existing intellectual property.

## Requirements

    Python 3.7+
    Django 3.2+
    PostgreSQL

## Installation

    Clone the repository
    Install the requirements pip install -r requirements.txt
    Set up the PostgreSQL database and update the database settings in settings.py
    Run the migrations python manage.py migrate
    Create a superuser python manage.py createsuperuser
    Start the development server python manage.py runserver

## Features

    Home page displaying the latest games
    Game detail page with description, screenshots, and ratings
    User registration and login
    User profile page with list of owned games and reviews
    Game search functionality
    Review system with star ratings and comments
    Admin panel for managing games, reviews, and users

## Usage

After starting the development server, navigate to http://localhost:8000 to view the home page. 

To leave a review, you must first register for an account and then log in. Once logged in, you can leave a star rating and comment on opinion page.

As an admin user, you can access the admin panel at http://localhost:8000/admin to manage games, reviews, and users.
Credits

This project was created by PlushaQ.
