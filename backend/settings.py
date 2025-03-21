import os
from pathlib import Path
import dj_database_url
import pymysql

pymysql.install_as_MySQLdb()


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-9jq_)f7ads+bdzb+@4=1br=^v7_(eu$hh9%q6*wvwcy#-%+d9s'


DEBUG = os.getenv("DEBUG", "False") == "True"

CORS_ALLOW_ALL_ORIGINS = True  # Solo para pruebas, en producción define dominios permitidos
ALLOWED_HOSTS = ['.onrender.com', 'localhost']

INSTALLED_APPS = [
     'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'rest_framework.authtoken',
    'django_filters',
    'rest_framework',
    'autenticacion',
    'accidente',
    'api',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}


ROOT_URLCONF = 'backend.urls'


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
            ],
        },
    },
]


WSGI_APPLICATION = 'backend.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'railway',  # Cambia esto al nombre real de tu BD en MySQL
        'USER': 'root',
        'PASSWORD': 'tXsaMSJUEjYCYQEiiTgefyDBeKOsqmGX',
        'HOST': 'trolley.proxy.rlwy.net',  # O la IP del servidor MySQL
        'PORT': '12478',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}



# DATABASES["default"] = dj_database_url.parse("postgresql://accidentes_y64i_user:U0n11283NpiaJ9yCD3BhTAdYDWsCTPti@dpg-csko9e2j1k6c73bkke9g-a.oregon-postgres.render.com/accidentes_y64i")


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Model Usuario
AUTH_USER_MODEL = 'autenticacion.Usuario'

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Seguridad en producción
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://tu-app.onrender.com']