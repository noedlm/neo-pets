"""
These are local settings that should not be in github, shared.
"""
import os


# SECURITY WARNING: keep the secret key used in production secret!
os.environ['SECRET_KEY'] = '{project secret key}'

# Database
os.environ['DATABASE_URL'] = 'postgres://url'

# pet finder API variables
os.environ['PETFINDER_BASE_URL'] = 'https://api.petfinder.com'
os.environ['PETFINDER_API_KEY'] = '{client id}'
os.environ['PETFINDER_API_SECRET'] = '{client secret}'
os.environ['PETFINDER_TOKEN_TYPE'] = 'Bearer'
os.environ['PETFINDER_ACCESS_TOKEN'] = ''

# google API
os.environ['GOOGLE_MAPS_API_KEY'] = '{api key}'