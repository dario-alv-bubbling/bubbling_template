"""
additional settings used in production
"""
BUBBLING_ENV = 'prod'

FRONTEND_HOST = 'https://bubbling.eu'

ALLOWED_HOSTS = ['...',
                 '127.0.0.1']

# For django storages
# AZURE_ACCOUNT_NAME = "******"
# AZURE_ACCOUNT_KEY = "******"
# AZURE_CONTAINER = "******"
# SHARE_URL = "******"
# AZURE_BLOB_CUSTOM_DOMAIN = "******"
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = '******'
# STATIC_URL = "https://%s/%s/" % (AZURE_BLOB_CUSTOM_DOMAIN,
#                                  STATICFILES_LOCATION)
# MEDIAFILES_LOCATION = 'mediafiles'
# DEFAULT_FILE_STORAGE = '******'
# MEDIA_URL = "https://%s/%s/" % (AZURE_BLOB_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
