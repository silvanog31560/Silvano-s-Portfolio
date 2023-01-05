from .base import *

ALLOWED_HOSTS = ['silvanogonzalez.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'os.environ.get("db_username")$os.environ.get("db_name")',
        'USER': 'os.environ.get("db_username")',
        'PASSWORD': 'os.environ.get("db_password")',
        'HOST': 'silvanogonzalez.mysql.pythonanywhere-services.com',
    }
}
