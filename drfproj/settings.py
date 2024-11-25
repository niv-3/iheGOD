import os
from pathlib import Path
import dj_database_url

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key (Set this securely in Heroku)
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')  # Use environment variable for production

# Debug mode (set from environment variable for safety)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed hosts for security (set your Heroku app's domain name here)
ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com', 'localhost']  # Replace with actual Heroku app name

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # Static files handling
    'drfapp',  # Your app
    'rest_framework',  # Django REST Framework
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'drfproj.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# WSGI Application
WSGI_APPLICATION = 'drfproj.wsgi.application'

# Database configuration (use PostgreSQL for Heroku)
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost')
}


# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration for Heroku (using WhiteNoise)
STATIC_URL = '/static/'  
STATIC_ROOT = BASE_DIR / 'staticfiles'  # WhiteNoise will use this for static files

# Security settings for production (ensure SSL and secure redirects)
SECURE_SSL_REDIRECT = True

import django_heroku
from whitenoise import WhiteNoise

# Activate Django-Heroku settings
django_heroku.settings(locals())

# Configure static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
