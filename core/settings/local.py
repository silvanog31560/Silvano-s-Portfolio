from .base import *

# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_URL = 'static/'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
