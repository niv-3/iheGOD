import os
from pathlib import Path

# Basic Django settings
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'your-secret-key'
DEBUG = False  # Turn off debug mode for production
ALLOWED_HOSTS = ['*']  # Adjust to your domain if needed

# Database configuration (default to SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # SQLite database
    }
}

# REST framework settings
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'drfapp',  # Your app where serializers are located
     
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

# Static and Media settings - Since you're not using static files, these can be removed or commented
STATIC_URL = '/static/'  # This is still needed for the reference in the project, but static files aren't served

# For media files (if you need to serve them)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Heroku-specific settings (assuming you're deploying to Heroku)
import django_heroku
django_heroku.settings(locals())  # Automatically adds production settings for Heroku deployment

# Security settings for production
SECURE_SSL_REDIRECT = True  # Redirect all HTTP to HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# Logging to track deployment issues
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Optional: CORS headers if you're using external APIs
CORS_ALLOW_ALL_ORIGINS = True  # Make sure to configure this more securely in production

# Django Rest Framework settings (optional)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
