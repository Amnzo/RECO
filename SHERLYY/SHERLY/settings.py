"""
Django settings for SHERLY project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h-@(^g(2lq2vqs+-pl1t-j(eh=3(w)5z)fj&y&plea=xdsc2=a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sherly_app',
    'crispy_forms',
    'wkhtmltopdf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'sherly_app.middleware.session_timeout.SessionTimeoutMiddleware',
]

ROOT_URLCONF = 'SHERLY.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sherly_app.context_processors.societer_info',  # Register your custom context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'SHERLY.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sherylstrategy$default',
        'USER': 'sherylstrategy',
        'PASSWORD': 'salmi@ensa123',
        'HOST': 'sherylstrategy.mysql.pythonanywhere-services.com',   # Or your MySQL server's hostname
        'PORT': '3306',        # Or your MySQL server's port
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SESSION_IDLE_TIMEOUT = 300    # 5 min
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_URL = '/login/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'sherly_app/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Email
EMAIL_BACKEND = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''
SERVER_EMAIL = ''
# Email

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.office365.com'
#EMAIL_HOST_USER = 'aslal-salmi@hotmail.fr'
#EMAIL_HOST_PASSWORD = 'mhphnqtwculehajq'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'aslal-salmi@hotmail.fr'
#SERVER_EMAIL = 'aslal-salmi@hotmail.fr'
#sherylopticalstrategy@hotmail.com
#vdqlnfmsvtwsusyf


# EMAIL_HOST_PASSWORD = ' UVQ6D-48EFA-5G6BG-MRURW-LKKA7'  # Mot de passe de votre compte Hotmail

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp-mail.outlook.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'aslal-salmi@hotmail.fr'  # Your Hotmail email address
# EMAIL_HOST_PASSWORD = 'UVQ6D-48EFA-5G6BG-MRURW-LKKA7'


#PDFKIT_CONFIG = {
 #  'wkhtmltopdf': 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
#}

PDFKIT_CONFIG = {
    'wkhtmltopdf': '/usr/bin/wkhtmltopdf'
}
# settings.py
print("---------------Starting-----------------")
# Celery Configuration


