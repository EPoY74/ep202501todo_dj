# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Добавляется ручками, rest api
    'rest_framework',  # Добавляется ручками
    # добавляю token authentication
    'rest_framework.authtoken',

    # мое todo приложение
    'app',


]