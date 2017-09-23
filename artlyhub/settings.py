import os
import _pickle as pickle

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

with open(os.path.join(BASE_DIR, 'sensitives.pickle'), 'rb') as f:
    sensitives = pickle.load(f)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = sensitives['secret_key']
IP_ADDRESS = sensitives['ip_address']
DB_NAME = sensitives['db_name']
DB_USER = sensitives['db_user']
DB_PW = sensitives['db_pw']

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = sensitives['debug']

ALLOWED_HOSTS = ['artlyhub.com',
                 'www.artlyhub.com',
                 IP_ADDRESS,
                 '127.0.0.1',
                 '127.0.1.1',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

    'accounts',
    'items',
    # 'likes',
    'restapi',
]

if not DEBUG:
    INSTALLED_APPS += [
        'django_celery_beat',
        'django_celery_results',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'artlyhub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'artlyhub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if DEBUG:
    HOST = IP_ADDRESS
else:
    HOST = 'localhost'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PW,
        'HOST': HOST,
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_DIR = os.path.join(BASE_DIR, 'static-dev/')
STATICFILES_DIRS = [
    os.path.join(STATIC_DIR, "css/dist"),
    os.path.join(STATIC_DIR, "js/dist"),
    os.path.join(STATIC_DIR, "img"),
    os.path.join(STATIC_DIR, "semantic/dist"),
    os.path.join(STATIC_DIR, "vendor/jquery/dist"),
    os.path.join(STATIC_DIR, "vendor/font-awesome/css"),
    os.path.join(STATIC_DIR, "vendor/font-awesome/fonts"),
]

MEDIA_URL = '/media/'
if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
else:
    MEDIA_ROOT = sensitives['media_root']

if not DEBUG:
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = TIME_ZONE

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        )
    }
