from .base import *
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['https://portafolio2-production.up.railway.app/']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
    #}
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'C22Zv7sszGBeWZd0mNww',
        'HOST': 'containers-us-west-174.railway.app',
        'PORT': '7131'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]