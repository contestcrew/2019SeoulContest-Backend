from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'db-first-person.crsxgsctsjxm.ap-northeast-2.rds.amazonaws.com',
        'USER': 'fastkim0909',
        'PASSWORD': 'rlavozoa12',
        'PORT': 5432,
    }
}