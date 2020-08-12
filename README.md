# Twitoff-dspt6

A basic application of Twitter responses using predictive analysis to determine user.

'''
<https://github.com/techthumb1/Twitoff-PT6.git>
cd twitoff-pt6/
'''

## Setup

'''
pipenv install
'''

Migrate the database:

'''
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
'''

## Usage

'''
FLASK_APP=web_app flask run
'''
