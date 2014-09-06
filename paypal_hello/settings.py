"""
Django settings for paypal_hello project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOG_DIR = os.path.join(BASE_DIR, 'log')
SERVER_FQDN = socket.getfqdn()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+*il&k0%6#b1_8t_#u+zz=%ueqg_cgi8kgbst2&h1rqt2ja9j7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',
    'paypal.standard.ipn',
)

# Paypal Settings
PAYPAL_RECEIVER_EMAIL = "d.miyakawa+paypal_hello@gmail.com"
# PAYPAL_TEST = True

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'paypal_hello.urls'

WSGI_APPLICATION = 'paypal_hello.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(levelname)7s %(asctime)s %(module)s %(process)d'
                       ' %(thread)d %(message)s')
        },
        'simple': {
            'format': '%(levelname)7s %(message)s'
        },
        'default': {
            'format': ('%(levelname)7s %(asctime)s'
                       ' %(module)s L%(lineno)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'debug': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'maxBytes': 20 * 1024 * 1024,
            'backupCount': 3,
            'formatter': 'default',
        },
    },
    'loggers': {
        'hello.debug': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
