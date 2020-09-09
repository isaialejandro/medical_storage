
import os

from .base import *


#RPI-DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '10.102.2.10',
        'NAME': 'medical_db',
        'PORT': 5432,
        'USER': 'medical_storage_admin',
        'PASSWORD': 'xD6itiei_99@!'
    }
}


STATIC_URL = '/static/'