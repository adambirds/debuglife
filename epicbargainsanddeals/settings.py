"""
Django settings for epicbargainsanddeals project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import logging
import os
from pathlib import Path
from typing import List

import django_stubs_ext

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SITE_URL = os.environ.get("SITE_URL", "http://localhost:8000")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-fdg2(_6j#^s=!x*$-t#f1q6y9bu-k-4i$xrsnuv%xn@xe_r(r2"
)

AMAZON_AFFILIATE_TAG = os.environ.get("AMAZON_AFFILIATE_TAG", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG", "0")))
DEBUG_TOOLBAR_ENABLED = bool(int(os.environ.get("DEBUG_TOOLBAR_ENABLED", "0")))

if DEBUG:
    # will output to your console
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

ALLOWED_HOSTS: List[str] = ["*"]


# Application definition

INSTALLED_APPS = [
    "apps.shop",
    "authentication",
    "jet",
    "drf_spectacular",
    "rest_framework",
    "knox",
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIGRATION_MODULES = {
    "jet": "apps.jet.migrations",
}

if DEBUG_TOOLBAR_ENABLED:
    INSTALLED_APPS += ["debug_toolbar"]

AUTH_USER_MODEL = "authentication.User"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "epicbargainsanddeals.pagination.CustomPageNumberPagination",
    "DEFAULT_AUTHENTICATION_CLASSES": ("knox.auth.TokenAuthentication",),
    "PAGE_SIZE": 100,
}

REST_KNOX = {"AUTH_HEADER_PREFIX": "Bearer", "TOKEN_TTL": None}

SPECTACULAR_SETTINGS = {
    "TITLE": "Epic Bargains And Deals API",
    "DESCRIPTION": "API for Epic Bargains And Deals",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_COERCE_PATH_PK_SUFFIX": True,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayRequestDuration": True,
    },
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG_TOOLBAR_ENABLED:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

AUTHENTICATION_BACKENDS = [
    "authentication.backends.EmailBackend",
]

ROOT_URLCONF = "epicbargainsanddeals.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": DEBUG,
        },
    },
]

WSGI_APPLICATION = "epicbargainsanddeals.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE", "epicbargainsanddeals"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

DEFAULT_DOMAIN = "http://localhost:8000/"

django_stubs_ext.monkeypatch()

X_FRAME_OPTIONS = "SAMEORIGIN"

CSRF_COOKIE_HTTPONLY = False

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://127.0.0.1:6379/0")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# CORS

CORS_ALLOWED_ORIGINS = [
    "https://epicbargainsanddeals.co.uk",
    "https://www.epicbargainsanddeals.co.uk",
]

if DEBUG:
    CORS_ALLOWED_ORIGINS += [
        "http://localhost:3000",
    ]

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "X-CSRFToken",
]

CORS_ALLOW_CREDENTIALS = True

SESSION_ENGINE = "authentication.redis_sessions.session"

SESSION_REDIS = {
    "host": "epicbargainsanddeals-redis",
    "port": 6379,
    "db": 0,
    "password": "",
    "prefix": "session",
    "socket_timeout": 1,
    "retry_on_timeout": False,
}

SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = True

if DEBUG:
    SESSION_COOKIE_SAMESITE = "None"
