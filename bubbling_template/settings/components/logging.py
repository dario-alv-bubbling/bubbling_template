"""
Place logstash,
        graylog, or
        sentry
here!
"""
import logging
from os import environ

DEBUG = environ.get('DEBUG', False) == 'TRUE'

if DEBUG:
    # https://stackoverflow.com/questions/4558879/python-django-log-to-console-under-runserver-log-to-file-under-apache
    # will output to your console
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    )
else:
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s %(levelname)s %(message)s',
    )
