"""
Relational, NoSQL and Object Relational Databases
Needs default database, but can user others
"""
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
from os import environ
import dj_database_url

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DB_PREFIX = 'bubbling_template_'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('DATABASE_NAME'),
        'USER': environ.get('DATABASE_USER'),
        'PASSWORD': environ.get('DATABASE_PASSWORD'),
        'HOST': environ.get('DATABASE_HOST'),
        'PORT': environ.get('DATABASE_PORT'),
        'CONN_MAX_AGE': int(environ.get('DATABASE_CONN_MAX_AGE', 600)),
        'OPTIONS': {
            'connect_timeout': int(environ.get('DATABASE_CONNECTION_TIMEOUT', 10)),
        },
    }
}

# For other database configurations
# (heroku: Update database configuration from $DATABASE_URL)
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
