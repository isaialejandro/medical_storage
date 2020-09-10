
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


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

STATIC_URL = '/static/'

