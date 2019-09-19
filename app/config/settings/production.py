from .base import *

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.application'

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DATABASES = secrets['DATABASES']