import os
from pathlib import Path
from decouple import config, Csv, AutoConfig

config = AutoConfig('envs')

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Production
CSRF_TRUSTED_ORIGINS = [f'https://{x}' for x in ALLOWED_HOSTS]

# Development nginx server
if DEBUG:
    CSRF_TRUSTED_ORIGINS = ['http://localhost:81']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zaza_interior.web.apps.WebConfig',

    "filer",
    "easy_thumbnails",
    "zaza_interior.gallery.apps.GalleryConfig",
    "django_recaptcha",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = 'zaza_interior.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'zaza_interior.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ("en", "English"),
    ("bg", "Bulgarian"),
]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
STATIC_ROOT = config('STATIC_ROOT')

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'mediafiles'))

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django filer configs
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

FILER_MIME_TYPE_WHITELIST = [
    "image/*",
    "video/*",
]

FILER_STORAGES = {
    'public': {
        'main': {
            'UPLOAD_TO': 'zaza_interior.gallery.helpers.upload_path',
        },
    },
}

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY', cast=str, default='')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY', cast=str, default='')
