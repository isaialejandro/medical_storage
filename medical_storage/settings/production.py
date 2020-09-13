from .base import *


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
#STATIC_ROOT = '/opt/django-on-docker/medicalStorage/medical_storage/medical_storage/staticfiles/'
STATIC_ROOT = '/medical_storage/staticfiles'

#MEDIA_ROOT =