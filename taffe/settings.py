"""
Django settings for taffe project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import environ
from pathlib import Path
import os
import taffe
import subprocess


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Commit git dans le numéro de version
try:
    GIT_COMMIT_HASH = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=BASE_DIR).decode(
        "utf-8").strip()
    GIT_COMMIT_DATE = subprocess.check_output(["git", "show", "-s", "--format=%cd", "--date=format:%d/%m/%Y"],
                                              cwd=BASE_DIR).decode("utf-8").strip()
    APP_VERSION_NUMBER = taffe.__version__ + " du " + GIT_COMMIT_DATE + " (" + GIT_COMMIT_HASH + ")"
except:
    APP_VERSION_NUMBER = taffe.__version__
	
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    SECURE_SSL_REDIRECT=(bool, True)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT')

ALLOWED_HOSTS = tuple(env.list('DJANGO_ALLOWED_HOSTS', default=[]))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apporteur.apps.ApporteurConfig',
    'assure.apps.AssureConfig',
    'assureur.apps.AssureurConfig',
    'courtier.apps.CourtierConfig',
    'tier.apps.TierConfig',
    'core.apps.CoreConfig',
    'interlocuteur.apps.InterlocuteurConfig',
    'gestion.apps.GestionConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'taffe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.selected_settings',

            ],
        },
    },
]

WSGI_APPLICATION = 'taffe.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE'),
		'HOST': env('DATABASE_HOST'),
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_USER_PASSWORD'),
        'PORT': env('DATABASE_PORT'),
    }
}
LOGIN_URL = '/connexion'
LOGIN_REDIRECT_URL = '/apporteur/apporteur-nouveau'
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_USER_MODEL = "core.Utilisateur"

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

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
