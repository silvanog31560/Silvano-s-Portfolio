from .base import *

ALLOWED_HOSTS = ['silvanogonzalez.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'silvanogonzalez$portfolio',
        'USER': 'silvanogonzalez',
        'PASSWORD': os.environ.get("db_password"),
        'HOST': 'silvanogonzalez.mysql.pythonanywhere-services.com',
    }
}
