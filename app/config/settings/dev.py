from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'

secrets = json.load(open(SECRETS_DIR, 'dev.json'))

