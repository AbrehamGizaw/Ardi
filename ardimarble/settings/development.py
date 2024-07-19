from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Security settings for development (usually more permissive)
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'SAMEORIGIN'
