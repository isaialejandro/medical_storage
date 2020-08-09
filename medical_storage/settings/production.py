from .base import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('MEDICAL_APP_SECRET_KEY')
#SECRET_KEY = 'l!5g7y24t8_iw9m9sppciq%)9mtoo5)=s+m_!wp*b-c7nw-@)3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', default=1))
#DEBUG = False

#ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS')   #LocalNetwork 10.64.236.0
ALLOWED_HOSTS = ['10.64.236.0']

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