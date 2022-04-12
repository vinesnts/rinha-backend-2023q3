import os

from dotenv import load_dotenv

from core.utils.utils import logstd

# Loads enviroment variables from .env
load_dotenv()

# Sets app name
APP_NAME = os.environ.get('APP_NAME')

# Sets debug mode on or off defined in the enviroment variables
DEBUG = os.environ.get('DEBUG', 'off') == 'on'

# JWT Token configuration
JWT_SECRET = os.environ.get('JWT_SECRET', 'secret')
JWT_ALGORITHM = 'HS256'

# Sets the project path defined in the enviroments variables
BASE_PATH = os.environ.get('BASE_PATH')

# Sets the base api url
BASE_URL = os.environ.get('BASE_URL', '/')

DATABASES = {
    'default': {
        'name': os.environ.get('DEFAULT_DB_NAME'),
        'host': os.environ.get('DEFAULT_DB_HOST'),
        'port': os.environ.get('DEFAULT_DB_PORT'),
        'user': os.environ.get('DEFAULT_DB_USER'),
        'password': os.environ.get('DEFAULT_DB_PASSWORD'),
    },
}

logstd(f'''
    {APP_NAME} started
    DEBUG: {'on' if DEBUG else 'off'}
    DATABASES: {DATABASES}
    BASE_PATH: {BASE_PATH}
''')