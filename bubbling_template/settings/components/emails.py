from os import environ

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = environ.get('EMAIL_HOST')
EMAIL_PORT = environ.get('EMAIL_PORT')
SENDER_EMAIL = 'info@bubbling.eu'
SENDER_NAME = 'The bubbling team'
