
import os

from .base import *


#HomeServer Prod DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '10.102.2.23',
        'NAME': 'medical_db',
        'PORT': 5432,
        'USER': 'medical_admin',
        'PASSWORD': 'f%_QgEoap!0'
    }
}


STATIC_URL = '/static/'