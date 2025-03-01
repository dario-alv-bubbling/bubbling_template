"""
Django settings for user_operator project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from os import environ, path
from bubbling_template.settings.components import BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    # project apps:
    # 'dummy',
    'core',
    # 'healthchecks',

    # default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Health checks:
    # You may want to enable other checks as well,
    # see: https://github.com/KristianOellegaard/django-health-check
    # 'health_check',
    # 'health_check.db',
    # 'health_check.cache',
    # 'health_check.storage',

    # Third party apps
    'rest_framework',
    # 'softdelete',
    'bubbling_firebase_authentication',
    # 'corsheaders',
    'drf_yasg',
    'storages'
]

MIDDLEWARE = [
    # 'corsheaders.middleware.CorsMiddleware',  # apply before WhiteNoise and CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    # "'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'corsheaders.middleware.CorsPostCsrfMiddleware',  # apply after CsrfViewMiddleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bubbling_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bubbling_template.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'bubbling_firebase_authentication.authentication.FirebaseAuthenticationAnonymous',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'bubbling_firebase_authentication.firebase_anonymous_permissions.IsAuthenticatedAnonymous',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

COMPANY_NAME = 'Bubbling'
COMPANY_SITE = 'https://bubbling.eu'

PAGINATION = {
    'PAGE_SIZE': 20,
    'MAX_PAGE_SIZE': 100,
    'PAGE_SIZE_QUERY_PARAM': 'page_size'
}

# CORS Headers configuration
# CORS_ALLOWED_ORIGIN_REGEXES = [
#    r'(http(s)?://)?localhost(:)?.*',
#    r'(http(s)?://)?127\.0\.0\.1(:)?.*'
# ]

# unlike CSRF_TRUSTED_ORIGINS, this setting does not allow you to distinguish between
# domains that are trusted to read resources by CORS and domains that are trusted to change resources
# by avoiding CSRF protection
# CORS_REPLACE_HTTPS_REFERER = True
