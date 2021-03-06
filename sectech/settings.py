"""
Django settings for sectech project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import dj_database_url
import os

from django.contrib.messages import constants as messages
from dotenv import load_dotenv
from pathlib import Path

# To use dotenv, ensure .env file is in same dir as this settings.py file
# env vars defined in .env will be exported to our runtime environment
# See .env_example file for example vars & structure
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR.joinpath('templates')

# DEBUG will always eval to False unless DEVELOPMENT var exists in .env
DEVELOPMENT = os.getenv('DEVELOPMENT', False)
DEBUG = DEVELOPMENT

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', 'localhost')]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if os.getenv('DATABASE_URL', False):
    DATABASES = {
        'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# CORS
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'storages',

    # Custom
    'home',
    'products',
    'shopping_cart',
    'customers',
    'checkout',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sectech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
            TEMPLATES_DIR/'allauth',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom
                'shopping_cart.contexts.cart_contents',
            ],
            # allow global use of template tags without need for {% load %}
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'sectech.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# 'en-gb' allows inputting dates in dd/mm/yy format
LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
MEDIA_ROOT = BASE_DIR.joinpath('media')
STATICFILES_DIRS = [BASE_DIR.joinpath('static'), ]

# AWS S3
if os.getenv('USE_AWS', False):
    # S3 Bucket Config
    # allow bucket & region option to be set in env
    AWS_STORAGE_BUCKET_NAME = os.getenv(
        'AWS_STORAGE_BUCKET_NAME', 'sectech-ci-pp5'
    )
    AWS_S3_REGION_NAME = os.getenv(
        'AWS_S3_REGION_NAME', 'eu-west-1'
    )
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'sectech.custom_storages.StaticStorage'
    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'sectech.custom_storages.MediaStorage'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


# Added these for the django-allauth package
# https://django-allauth.readthedocs.io/en/latest/installation.html
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
# user registraion email confirmation
if DEVELOPMENT:
    # Log emails to the console during development
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST_USER = 'sectech.app@example.com'
else:
    # send mail using SMTP AUTH client
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    # default to SMTP with STARTTLS
    EMAIL_PORT = os.getenv('EMAIL_PORT', 587)
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', True)

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SITE_ID = 1

# Hook into the user allauth login mechanism to override default behaviour
# https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-redirects
ACCOUNT_ADAPTER = 'customers.adapter.CustomAccountAdapter'

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Django messages constants with Bootstrap classes
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}


# Stripe payments
STRIPE_CURRENCY = os.getenv('STRIPE_CURRENCY', 'eur')
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_ENDPOINT_SECRET = os.getenv('STRIPE_ENDPOINT_SECRET')
