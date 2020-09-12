
import os

from .base import *

DEBUG = int(os.environ.get('DEBUG', default=0))

#HomeServer Prod DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST'),
        'NAME': os.getenv('DB_NAME'),
        'PORT': os.getenv('DB_PORT'),
        'USER': os.getenv('DB_USR'),
        'PASSWORD': os.getenv('DB_PWD')
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]