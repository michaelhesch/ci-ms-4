"""
Django settings for liffey project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import environ
import os
import dj_database_url

# Init environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Get secret key from environment
SECRET_KEY = env('SECRET_KEY')

# Get development setting flag in environment
DEBUG = env('DEVELOPMENT')

ALLOWED_HOSTS = [
    'ci-ms-4-mh.herokuapp.com',
    'localhost',
    '127.0.0.1'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'crispy_forms',
    'django_countries',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home.apps.HomeConfig',
    'product.apps.ProductConfig',
    'profiles.apps.ProfilesConfig',
    'checkout.apps.CheckoutConfig',
    'cart.apps.CartConfig',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'liffey.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
            os.path.join(BASE_DIR, 'product', 'templates', 'product'),
            os.path.join(BASE_DIR, 'home', 'templates', 'home'),
            os.path.join(BASE_DIR, 'profiles', 'templates', 'profiles'),
            os.path.join(BASE_DIR, 'checkout', 'templates', 'checkout'),
            os.path.join(BASE_DIR, 'cart', 'templates', 'cart'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # Request required by Allauth to access request object
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'cart.contexts.cart_contents',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
                'django.contrib.humanize.templatetags.humanize',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Site ID required by Allauth for social meida account login
SITE_ID = 1

# Account registration settings
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4

# Login routing settings
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'


WSGI_APPLICATION = 'liffey.wsgi.application'


# HTTPS security settings
# Prevents session cookie being transmitted via HTTP accidentally
SESSION_COOKIE_SECURE = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if 'DATABASE_URL' in env:
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Production environment static files and AWS settings
if 'USE_AWS' in env:
    # Configure cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # AWS Bucket config
    AWS_STORAGE_BUCKET_NAME = 'ci-ms-4-mh'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media file storage
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override and set static & media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Set Crispyforms to use Bootstrap 4 templates
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Media file directory settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Stripe configuration
SELLING_FEE_PERCENTAGE = 5
FREE_DELIVERY_THRESHOLD = 99
STRIPE_CURRENCY = 'USD'
STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_WH_SECRET = env('STRIPE_WH_SECRET')

if env('DEVELOPMENT'):
    # Development environment email settings
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'liffeyshop@example.com'
else:
    # Production environment email settings
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = env('EMAIL_HOST_USER')
