"""
Django settings for {{cookiecutter.project_name}} project.

Generated by 'django-admin startproject' using Django.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import os
import string

from configurations import Configuration, values


class ProjectDefault(Configuration):
    """
    The default settings from the Django project template.

    Django Configurations
    https://django-configurations.readthedocs.io
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(True)

    ALLOWED_HOSTS = values.ListValue([])

    # Application definition

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "{{cookiecutter.project_slug}}.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ]
            },
        }
    ]

    WSGI_APPLICATION = "{{cookiecutter.project_slug}}.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/stable/ref/settings/#databases

    DATABASES = values.DatabaseURLValue()

    # Password validation
    # https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators
    # fmt: off
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
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
    # fmt: on
    # Internationalization
    # https://docs.djangoproject.com/en/stable/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/stable/howto/static-files/

    STATIC_URL = "/static/"

    STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "static"))

    STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
    )

    # Stored files
    # https://docs.djangoproject.com/en/stable/topics/files/{% if cookiecutter.use_media_volume == "Yes" %}  # noqa

    MEDIA_URL = "/media/"

    MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, "media"))  # noqa{% else %}

    # MEDIA_URL = "/media/"

    # MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, "media")){% endif %}

    # Email Settings
    # https://docs.djangoproject.com/en/stable/topics/email/
    # fmt: off
    ADMINS = values.SingleNestedTupleValue((("admin", "errors@{{cookiecutter.domain_url}}"),))  # noqa
    # fmt: on
    DEFAULT_FROM_EMAIL = values.EmailValue("info@{{cookiecutter.domain_url}}")

    EMAIL_SUBJECT_PREFIX = "[{{cookiecutter.project_name}}] "

    EMAIL_USE_LOCALTIME = True

    SERVER_EMAIL = values.EmailValue("server@{{cookiecutter.domain_url}}")

    # Email URL
    # https://django-configurations.readthedocs.io/en/stable/values/

    EMAIL = values.EmailURLValue("console://")

    # Translation
    # https://docs.djangoproject.com/en/stable/topics/i18n/translation/

    # LANGUAGES = (("en", "English"), ("it", "Italiano"))

    # LOCALE_PATHS = (os.path.abspath(os.path.join(BASE_DIR, "locale")),)


class Local(ProjectDefault):
    """The local settings."""

    # Application definition

    INSTALLED_APPS = ProjectDefault.INSTALLED_APPS.copy()

    MIDDLEWARE = ProjectDefault.MIDDLEWARE.copy()

    # Django Debug Toolbar
    # https://django-debug-toolbar.readthedocs.io/en/stable/configuration.html

    try:
        import debug_toolbar  # noqa
    except ModuleNotFoundError:  # pragma: no cover
        pass
    else:  # pragma: no cover
        INTERNAL_IPS = values.ListValue([], environ_name="ALLOWED_HOSTS")
        INSTALLED_APPS.append("debug_toolbar")
        MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")


class Testing(ProjectDefault):
    """The testing settings."""

    SECRET_KEY = string.ascii_letters

    # Debug
    # https://docs.djangoproject.com/en/stable/ref/settings/#debug

    DEBUG = False

    # Email URL
    # https://django-configurations.readthedocs.io/en/stable/values/

    EMAIL = "dummy://"


class Remote(ProjectDefault):
    """The remote settings."""

    # Sentry
    # https://sentry.io/for/django/

    try:
        import sentry_sdk  # noqa
        from sentry_sdk.integrations.django import DjangoIntegration  # noqa
    except ModuleNotFoundError:  # pragma: no cover
        pass
    else:  # pragma: no cover
        sentry_sdk.init(
            integrations=[DjangoIntegration()], send_default_pii=True,
        )


class Development(Remote):
    """The development settings."""

    # Debug
    # https://docs.djangoproject.com/en/stable/ref/settings/#debug

    DEBUG = True


class Integration(Remote):
    """The integratrion settings."""

    # Debug
    # https://docs.djangoproject.com/en/stable/ref/settings/#debug

    DEBUG = False


class Production(Remote):
    """The production settings."""

    # Debug
    # https://docs.djangoproject.com/en/stable/ref/settings/#debug

    DEBUG = False

    # Email URL
    # https://django-configurations.readthedocs.io/en/stable/values/

    EMAIL = values.EmailURLValue()

    # Security
    # https://docs.djangoproject.com/en/stable/topics/security/

    SECURE_BROWSER_XSS_FILTER = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = "DENY"  # Default: 'SAMEORIGIN'

    # Persistent connections
    # https://docs.djangoproject.com/en/stable/ref/databases/#general-notes

    # CONN_MAX_AGE = None
