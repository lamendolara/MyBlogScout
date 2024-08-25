from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Add your allowed hosts here
ALLOWED_HOSTS = ['46.101.136.86']  # ['your_domain.com', 'your_ip_address']Cambia esto por tu dominio o IP del servidor

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',  # Cambia esto si usas un host diferente
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.child('staticfiles')  # Directorio para archivos estáticos en producción

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# Ckeditor settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
TOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'Format', 'FontSize', 'Link'],
            ['Smiley', 'Image', 'Iframe'],
            ['RemoveFormat', 'Source'],
        ],
        'stylesSet': [],
    }
}

# Additional security settings
# Use strong settings for production
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SESSION_COOKIE_SECURE = True  # Usar solo en HTTPS
# CSRF_COOKIE_SECURE = True  # Usar solo en HTTPS
# SECURE_HSTS_SECONDS = 3600  # 1 hora
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
