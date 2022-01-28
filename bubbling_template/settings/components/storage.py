"""
Static files serving, media folders and S3 configs
"""
from os import environ, path
from bubbling_template.settings import USE_S3
from bubbling_template.settings.components import BASE_DIR

# SERVING MEDIA AND STATIC FILES (https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/)
# Media files
# Media root dir is commonly changed in production
# (see development.py and production.py).
# https://docs.djangoproject.com/en/3.1/topics/files/

# The URL to use when referring to static files (where they will be served from)
# USE_S3 is set on __init__.py
if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    # s3 static settings (in order to store site content...)
    # STATIC_LOCATION = 'static'
    # STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    # STATICFILES_STORAGE = 'common.storage_backends.StaticStorage'

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'core.storage_backends.PublicMediaStorage'
else:
    MEDIA_URL = '/mediafiles/'
    MEDIA_ROOT = path.join(BASE_DIR, 'mediafiles')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),) # TODO: investigate: https://stackoverflow.com/questions/41904685/oserror-errno-2-no-such-file-or-directory-tmp-makecalls-static

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
