# Pick as you wish

A small app using flask-restful to create api endpoints that will be used as a pick your own story via postman.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The things you need before installing the software.

* create a new env $ python -m venv env
* activate your env $ source env/bin/activate
* install requirements $ pip install -r requirements.txt
* have postman installed on your computer

### Installation

at the root of the project with the env activated run $ python3 api.py
the app should now listen to port 5000


## Usage

Go the postman and create a new POST request to http://localhost:5000/start, you will see in the response a 'story' key narrating the story and a 'choose' key with the available options to continue.
To continue the story create another POST request to http://localhost:5000/choose, send a body containin a json with 'option' key and an integer according to the selection option.
Again you will see in the response a 'story' key narrating the story and, if available, a 'choose' key with the available options to continue.