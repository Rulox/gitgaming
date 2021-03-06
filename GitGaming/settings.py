"""
Django settings for GitGaming project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from easy_thumbnails.conf import Settings as thumbnail_settings
from GitGaming.settings_production import DEBUG as PROD_DEBUG
from GitGaming.settings_production import TEMPLATE_DEBUG as PROD_TEMPLATE_DEBUG
import requests_cache

requests_cache.install_cache('test_cache', backend='sqlite', expire_after=6000)  # Cache

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
BROKER_URL = 'redis://localhost:6379/0'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
SECRET_KEY = 'changethis'

#from GitGaming.settings_production import DEBUG as PRODUCTION_DEBUG, TEMPLATE_DEBUG as PRODUCTION_TEMPLATE_DEBUG
DEBUG = PROD_DEBUG
TEMPLATE_DEBUG = PROD_TEMPLATE_DEBUG
SITE_ID = 1



ALLOWED_HOSTS = []

""" Social Keys for AUTH """
""" DEBUG ONLY """
try:
    from SECRET import *
    SOCIAL_AUTH_GITHUB_KEY = GITHUB1
    SOCIAL_AUTH_GITHUB_SECRET = GITHUB2
except ImportError:
    SOCIAL_AUTH_GITHUB_KEY = ""
    SOCIAL_AUTH_GITHUB_SECRET = ""
    pass

# Cropping images
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Locales
    'developers',
    'badges',
    'stats',
    'worker',
    'skills',
    # Externas
    'django_extensions',
    'easy_thumbnails',
    'image_cropping',
    'pygithub3',
    'social.apps.django_app.default',
    'crispy_forms',
    'zinnia_bootstrap',
    'tagging',
    'mptt',
    'django.contrib.sites',
    'django_comments',
    'zinnia',
    'ckeditor',
    'zinnia_ckeditor',
    'modeltranslation',
)

CKEDITOR_CONFIGS = {
    'zinnia-content': {
        'toolbar_Zinnia': [
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Undo', 'Redo'],
            ['Scayt'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Source'],
            ['Maximize'],
            '/',
            ['Bold', 'Italic', 'Underline', 'Strike',
             'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-',
             'Outdent', 'Indent', '-', 'Blockquote'],
            ['Styles', 'Format'],
        ],
        'toolbar': 'Zinnia',
    },
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'GitGaming.urls'

WSGI_APPLICATION = 'GitGaming.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap3' #Crispy Forms template


AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

from django.utils.translation import ugettext_lazy as _

# LANGUAGE

LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "GitGaming/media")
MEDIA_URL = "/media/"
CKEDITOR_UPLOAD_PATH = MEDIA_URL

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'zinnia.context_processors.version',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'developers.models.save_user',  # <--- set the import-path to the function
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

ZINNIA_FEEDS_FORMAT = 'atom'

LOGIN_REDIRECT_URL = '/'

TEMPLATE_LOADERS = [
  'app_namespace.Loader',
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  'django.template.loaders.eggs.Loader',
]


# Production STUFF
if not DEBUG:
    from settings_production import DATABASES, SECRET_KEY, STATIC_ROOT, ALLOWED_HOSTS
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
