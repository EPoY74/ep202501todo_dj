from pathlib import Path  ##
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Это твой секретный ключ'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# docker run --name todo-postgres -p 5432:5432 -e POSTGRES_PASSWORD=PassWord -d postgres


DB_ENGINE =  'django.db.backends.sqlite3'
DB_NAME = BASE_DIR / 'db.sqlite3'

DB_ENGINE_PG = 'django.db.backends.postgresql'
DB_NAME_PG = 'Имя базы данных'
DB_USER_PG = 'Пользователь БД'
DB_PASSWORD_PG = 'Пароль БД'
DB_HOST_PG = 'Хост БД'
DB_PORT_PG = 'Порт в БД'

