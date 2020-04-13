from .local import *
DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'twoscoops',
            'HOST': 'localhost',
        }
}
INSTALLED_APPS += ['debug_toolbar', ]
