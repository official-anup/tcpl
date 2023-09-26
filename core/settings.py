"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os, random, string, inspect
from pathlib import Path
from dotenv import load_dotenv
import boto3
from storages.backends.s3boto3 import S3Boto3Storage

import django_dyn_dt

load_dotenv()  # take environment variables from .env.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))

# Render Deployment Code
DEBUG = 'RENDER' not in os.environ

# HOSTs List
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Add here your deployment HOSTS
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://localhost:5085', 'http://127.0.0.1:8000', 'http://127.0.0.1:5085']

X_FRAME_OPTIONS = "SAMEORIGIN"

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'admin_datta.apps.AdminDattaConfig',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
'django.contrib.gis',
"storages",
    "home",

    # Tooling Dynamic_DT
    'django_dyn_dt',             # <-- NEW: Dynamic_DT

    # Tooling API-GEN
    'django_api_gen',            # Django API GENERATOR  # <-- NEW
    'rest_framework',            # Include DRF           # <-- NEW 
    'rest_framework.authtoken',  # Include DRF Auth      # <-- NEW     
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

HOME_TEMPLATES      = os.path.join(BASE_DIR, 'templates') 
TEMPLATE_DIR_DATATB = os.path.join(BASE_DIR, "django_dyn_dt/templates") # <-- NEW: Dynamic_DT

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [HOME_TEMPLATES, TEMPLATE_DIR_DATATB],                  # <-- UPD: Dynamic_DT
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
# DB_USERNAME = os.getenv('DB_USERNAME' , None)
# DB_PASS     = os.getenv('DB_PASS'     , None)
# DB_HOST     = os.getenv('DB_HOST'     , None)
# DB_PORT     = os.getenv('DB_PORT'     , None)
# DB_NAME     = os.getenv('DB_NAME'     , None)

# if DB_ENGINE and DB_NAME and DB_USERNAME:
#     DATABASES = { 
#       'default': {
#         'ENGINE'  : 'django.db.backends.' + DB_ENGINE, 
#         'NAME'    : postgres,
#         'USER'    : postgres,
#         'PASSWORD': 123,
#         'HOST'    : localhost,
#         'PORT'    : 5432,
#         }, 
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': 'db.sqlite3',
#         }
#     }

# settings.py
GEOGRAPHY_DB_SRID = 4326

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        
        'NAME': 'database1',
        'USER': 'postgres', 
        'PASSWORD': '12345678',
        'HOST': 'data.c3unf3q1zfkv.ap-south-1.rds.amazonaws.com',
        'PORT': '5432',
       
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DYN_DB_PKG_ROOT = os.path.dirname( inspect.getfile( django_dyn_dt ) ) # <-- NEW: Dynamic_DT

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(DYN_DB_PKG_ROOT, "templates/static"),                # <-- NEW: Dynamic_DT 
)

#if not DEBUG:
#    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = '/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ### DYNAMIC_DATATB Settings ###
DYNAMIC_DATATB = {
    # SLUG -> Import_PATH 
    'product'  : "home.models.Product",
}
########################################

# ### API-GENERATOR Settings ###
API_GENERATOR = {
    # SLUG -> Import_PATH 
    'product'  : "home.models.Product",
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}
########################################

# GDAL_LIBRARY_PATH = 'C:/Users/91766/Desktop/zone1/.env/Lib/site-packages/osgeo/gdal304.dll' 
# GEOS_LIBRARY_PATH = 'C:/Users/91766/Desktop/zone1/.env/Lib/site-packages/osgeo/geos_c.dll'

# C:\Users\91766\Desktop\zone1\.env\Lib\site-packages\osgeo

# C:\Users\91766\Desktop\zone1\zone1\Lib\site-packages\osgeo



AWS_ACCESS_KEY_ID = 'AKIA4VYMO2FKZCLUCFHT '
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'tcplpostgres'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
