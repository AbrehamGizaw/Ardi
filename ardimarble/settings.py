"""
Django settings for ardimarble project.

Generated by 'django-admin startproject' using Django 3.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e0o*1xow1)a&2$8+j4ww0v$r((dp!&0z02_#1xhq%dpty0@y88'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ardi',
    'useracc',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'ardimarble.middleware.AutoLogoutMiddleware',

]


# settings.py

# Set the session engine to database-backed sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # or any other session backend you are using

# Set the session to expire after 1 hour (3600 seconds)
SESSION_COOKIE_AGE = 600  # 1 hour in seconds

# Ensure the session is saved every time it is modified
SESSION_SAVE_EVERY_REQUEST = True

# Optionally, you can also set the session to expire when the user closes their browser
SESSION_EXPIRE_AT_BROWSER_CLOSE = True




ROOT_URLCONF = 'ardimarble.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this line
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


WSGI_APPLICATION = 'ardimarble.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# login url
LOGIN_URL = '/useracc/login/'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

AUTH_USER_MODEL = 'useracc.CustomUser'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '1127',
#         'HOST': 'localhost',  # Set to 'localhost' if running locally
#         'PORT': '5432',  # Default PostgreSQL port
#     }
# }


# EMAIL_HOST='smtp.gmail.com'
# EMAIL_PORT = '587'
# EMAIL_HOST_USER='compacct01@gmail.com'
# EMAIL_FROM ='compacct01@gmail.com'
# EMAIL_HOST_PASSWORD='qxnwvesqfznyozbw'
# EMAIL_USE_TLS=True
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'ardimarble2@gmail.com'
# EMAIL_HOST_PASSWORD = 'oitg hvnm mqmj phrq'
# DEFAULT_FROM_EMAIL = 'ardimarble2@gmail.com'
EMAIL_HOST_USER='ardimarble2@gmail.com'
EMAIL_FROM ='ardimarble2@gmail.com'
EMAIL_HOST_PASSWORD='oitg hvnm mqmj phrq'

# EMAIL_HOST_USER='compacct01@gmail.com'
# EMAIL_FROM ='compacct01@gmail.com'
# EMAIL_HOST_PASSWORD='qxnwvesqfznyozbw'


