"""
Django settings for GitGaming project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import requests_cache
from easy_thumbnails.conf import Settings as thumbnail_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
requests_cache.install_cache('test_cache', backend='sqlite', expire_after=3000)  # Cache


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
SECRET_KEY = 'changethis'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    SITE_ID = 1


TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

""" Social Keys for AUTH """
""" DEBUG ONLY """
from SECRET import *
SOCIAL_AUTH_GITHUB_KEY = GITHUB1
SOCIAL_AUTH_GITHUB_SECRET = GITHUB2


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
    # Externas
    'django_extensions',
    'easy_thumbnails',
    'image_cropping',
    'pygithub3',
    'social.apps.django_app.default',
    'crispy_forms',
    'zinnia',
    'tagging',
    'mptt',
    'django.contrib.sites',
    'django_comments',
)

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

LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "GitGaming/media")
MEDIA_URL = "/media/"

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

LOGIN_REDIRECT_URL = '/'

# Production STUFF
if not DEBUG:
    from settings_production import *
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
