# ardimarble/settings/production.py

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ardimarble.com', 'www.ardimarble.com', '127.0.0.1', 'localhost']

# Security settings
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# Add any additional production-specific settings here
