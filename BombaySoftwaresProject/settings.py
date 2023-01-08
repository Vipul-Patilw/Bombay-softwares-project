"""
Django settings for BombaySoftwaresProject project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import  os
from pathlib import Path
from django.contrib.messages import constants as messages
from .info import *
from django.urls import resolve

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = Path(__file__).resolve().parent





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#r(@@=oweotyjsxmk#9o_$i#p-be^%5-y+6m0d@at-4$+3k77y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'BombaySoftwares.apps.BombaySoftwaresConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_flatpickr',
    'mailqueue',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

#AUTHENTICATION_BACKENDS = [
#    'django.contrib.auth.backends.ModelBackend',
#    'allauth.account.auth_backends.AuthenticationBackend',   
#]
#SITE_ID=1

ROOT_URLCONF = 'BombaySoftwaresProject.urls'

TEMPLATES = [
{ 
        'BACKEND':'django.template.backends.jinja2.Jinja2',
	'DIRS': [ PROJECT_DIR / 'jinjatemplates' ],
        'APP_DIRS': True,
        'OPTIONS':{
        "environment": "BombaySoftwares.jinja2.environment",
        'context_processors':[
          'BombaySoftwares.context.context_data',
                  'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 'social_django.context_processors.backends', 
          
]}
        },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #    'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
 
 
               

            ],
        },
    },
]

WSGI_APPLICATION = 'BombaySoftwaresProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

#PostgresSql Connection

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,"static/"),)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#STATIC_URLFILES_DIR = '/BombaySoftwaresProject/static/'

#STATIC_ROOT = BASE_DIR / "static"

# MEDIA_URL = 'media/'  

# #MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  
MEDIA_ROOT = BASE_DIR / "media"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'logout-page'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# If you're using Celery, set this to True
MAILQUEUE_CELERY = True

# Enable the mail queue. If this is set to False, the mail queue will be disabled and emails will be 
# sent immediately instead.
MAILQUEUE_QUEUE_UP = True

# Maximum amount of emails to send during each queue run
MAILQUEUE_LIMIT = 50

# If MAILQUEUE_STORAGE is set to True, will ignore your default storage settings
# and use Django's filesystem storage instead (stores them in MAILQUEUE_ATTACHMENT_DIR) 
MAILQUEUE_STORAGE = False
MAILQUEUE_ATTACHMENT_DIR = 'mailqueue-attachments'

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER =EMAIL_HOST_USER
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_PORT= EMAIL_PORT
EMAIL_HOST_PASSWORD=EMAIL_HOST_PASSWORD

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

#bombaysoftwares
#bombaysoftwares-374013
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '655898094440-pbqqv8s0ircbgv1tj3k348abgblhm0sp.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
# AUTH_USER_MODEL = 'BombaySoftwares.UserRegistration'

STATICFILES_STORAGE = 'BombaySoftwaresProject.storage.S3Storage'
