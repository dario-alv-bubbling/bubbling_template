from os import environ

SERVICE_ACCOUNT_KEY_FILE = {
    'type': 'service_account',
    'project_id': environ.get('FIREBASE_PROJECT_ID'),
    'private_key_id': environ.get('FIREBASE_PRIVATE_KEY_ID'),
    'private_key': environ.get('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    'client_email': environ.get('FIREBASE_CLIENT_EMAIL'),
    'client_id': environ.get('FIREBASE_CLIENT_ID'),
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': 'https://oauth2.googleapis.com/token',
    'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
    'client_x509_cert_url': environ.get('FIREBASE_CLIENT_X509_CERT_URL')
}

FIREBASE_AUTH = {
    'SERVICE_ACCOUNT_KEY_FILE': SERVICE_ACCOUNT_KEY_FILE,
    # require that user has verified their email
    'EMAIL_VERIFICATION': False
}

FIREBASE_API_KEY = environ.get('FIREBASE_API_KEY')
