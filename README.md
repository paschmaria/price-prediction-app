# Price Prediction App

A set of API endpoints and AutoML Pipelines for predicting the price of cars

## Getting started

These instructions will help get a copy of this project up and running on your local machine in no time.

### Prerequisites

What you will need you will need to run this app successfully:
```
Python 3.7.x

Django 3.0.x

PostgreSQL 12.2
```

### Installation

You can install and setup this project locally using the following steps:

Download the app
```
git clone https://github.com/paschmaria/price-prediction-app.git

cd price-prediction-app
```

Setup a virtual environment (Ubuntu OS)
```
virtualenv venv

source venv/bin/activate
```

Create a `local.env` file in the `env` directory

Create database and add DB settings to the `local.env` file

Update the following on the `local.env` file:
```
DJANGO_SETTINGS_MODULE=core.settings.local

SECRET_KEY=YOUR_SECRET_KEY

DEBUG_VALUE=True
```

Install requirements
```
pip install -r requirements.txt
```

Update DB and run app
```
python manage.py migrate

python manage.py runserver
```

## API Documentation

Documentation for the API endpoints can be found [here](https://documenter.getpostman.com/view/3999319/SzmfYx5R?version=latest)
