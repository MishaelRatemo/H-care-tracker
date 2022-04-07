"""
Django settings for hcaretracter project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
import  cloudinary
import cloudinary.uploader
import  cloudinary.api
import dj_database_url
import  django_heroku
from  decouple import  config,Csv


SECRET_KEY='django-insecure-#+nllh_^r_$kk21iw71bx4wuz^h21+*4uvn0!ub(4jwf59dz&o'
# SECRET_KEY='django-insecure-#+nllh_^r_$kk21iw71bx4wuz^h21+*4uvn0!ub(4jwf59dz&o'
MODE=config("MODE",default='dev')
SECRET_KEY=config('SECRET_KEY')
DEBUG=config('DEBUG',default=True, cast=bool)
#developemnt mode
if config('MODE')=='dev':
    DATABASES={
        'default':{
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': config('DB_NAME'),
           'USER': config('DB_USER'),
           'PASSWORD': config('DB_PASSWORD'),
           'HOST': config('DB_HOST'),
           'PORT': '',
        }
    }
#production mode
else:
     DATABASES = {
       'default': dj_database_url.config(
           default=config('DATABASE_URL')
       )
   }
    
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY= 'django-insecure-#+nllh_^r_$kk21iw71bx4wuz^h21+*4uvn0!ub(4jwf59dz&o'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG=True

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = [
    'fontawesomefree',  
    'bootstrap5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_registration',
    'corsheaders',
    'tracker',
    'donor',
    'about',
    'contact',
    'services',    
    'hospital',     
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    
    'corsheaders.middleware.CorsMiddleware',
    
]

ROOT_URLCONF = 'hcaretracter.urls'

DATABASES={
        'default':{
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': config('DB_NAME'),
           'USER': config('DB_USER'),
           'PASSWORD': config('DB_PASSWORD'),
           'HOST': config('DB_HOST'),
           'PORT': '5432',
        }
    }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],        
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

WSGI_APPLICATION = 'hcaretracter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = 'static/'
STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static'),]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# django_heroku.settings(locals())

MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')



# SECRET_KEY =os.environ.get('SECRET_KEY')
SECRET_KEY =os.environ.get('SECRET_KEY')
ACCOUNT_ACTIVATION_DAYS= os.environ.get('ACCOUNT_ACTIVATION_DAYS')
DEFAULT_FROM_EMAIL=os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST=os.environ.get('EMAIL_HOST')
EMAIL_PORT= os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS=True


cloudinary.config(
    cloud_name='mishmish',
    api_key='739237125342173',
    api_secret='0m3FpTW7VNcn3l6_bcja3ztpscw',
)



'''
*************************
'''
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.TokenAuthentication',
   ),
}

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGIN_REGEXES = [
r"^https://\w+\.domain\.com$",
]


# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000'
# ]
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:3000',
# )
# CSRF_TRUSTED_ORIGINS = [
#     'http://localhost:3000',
# ]


'''
for heroku userbelow configs

'''
# CORS_ALLOWED_ORIGINS = [
#     'https://h-care-tracker.herokuapp.com/'
# ]
