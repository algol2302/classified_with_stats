import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    #
    'rest_framework',
    # 
    'core',
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

ROOT_URLCONF = 'dj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'dj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'classified_db'),
        'USER': os.environ.get('POSTGRES_USER', 'classified_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '123456'),
        'HOST': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.environ.get('POSTGRES_PORT', 5432)
    }
    # about using infi.clickhouse_orm in django:
    # https://github.com/Infinidat/infi.clickhouse_orm/issues/124
}

# 
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 100
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Krasnoyarsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# 
REDIS_HOST = os.environ.get(
    'REDIS_HOST', '127.0.0.1'
)

REDIS_PORT = int(
    os.environ.get('REDIS_PORT', 6379),
)

LOCATION_CACHE = f'{REDIS_HOST}:{REDIS_PORT}'

# BACKEND_CACHE = 'redis_cache.cache.RedisCache'
#
# CACHES = {
#     'default': {
#         'BACKEND': BACKEND_CACHE,
#         'LOCATION': LOCATION_CACHE,
#         'OPTIONS': {
#             'DB': 1,
#         },
#     },
#     'city': {
#         'BACKEND': BACKEND_CACHE,
#         'LOCATION': LOCATION_CACHE,
#         'TIMEOUT': 60 * 60 * 24,
#         'OPTIONS': {
#             'DB': 2,
#         },
#     },
#     'advert': {
#         'BACKEND': BACKEND_CACHE,
#         'LOCATION': LOCATION_CACHE,
#         'TIMEOUT': 60 * 60 * 1,
#         'OPTIONS': {
#             'DB': 3,
#         },
#     }
# }

# 
DEBUG_TOOLBAR = True

if DEBUG_TOOLBAR:
    INSTALLED_APPS.extend(
        [
            'debug_toolbar',
        ]
    )
    MIDDLEWARE.extend(
        [
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]
    )
    
    INTERNAL_IPS = ['127.0.0.1']

# 
AUTH_USER_MODEL = 'core.CustomUser'

