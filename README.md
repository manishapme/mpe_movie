# My Place For Everything Movies

This is a small python application which will display information and ratings about movies I have seen. It is meant to be the beginning of a set of modules that will allow someone to track their thoughts about all kinds of media: books, music, movies and more.

## Getting Started

The system is pure python with a little bit of Bootstrap for front-end formatting. If you have python installed and can run a web-server, you need only to populate the seed data to get up and running.

### Prerequisites

Have Python 2.7.13 >= <3.0 installed.

Have pip installed

Install `virtualenv` with pip ```[sudo] pip install virtualenv``` 

### Installing

Git clone repo

Navigate to correct directory `cd mpe_movie`

Set up virtual environment```virtualenv env```

Activate virtual environment ```source env/bin/activate```

Install requirements ```pip install -r requirements.txt```

Populate `movie_data.py` with a list of movie objects following the format given.

### Running

To run simply execute ```python media_center.py``` in your console.

## Built With

Python

Jinja2

Bootstrap

## Authors
* **Manisha Patel** - *Initial work* - [manishapme](https://github.com/manishapme)

## Acknowledgments
Extends https://github.com/adarsh0806/ud036_StarterCode/