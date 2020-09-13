from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '10.64.2.23',
        'NAME': 'medical_db',
        'PORT': 5432,
        'USER': 'medical_admin',
        'PASSWORD': 'f%kdfkj_0092!'
    }
}
"""

"""
#RPI-DB FOR TEST
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
"""

STATIC_ROOT = '/opt/django-on-docker/medicalStorage/medical_storage/medical_storage/staticfiles/'
#MEDIA_ROOT =