
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SITE_ID = 1
DEBUG = True
TEMPLATE_DEBUG=DEBUG
ALLOWED_HOSTS = ['']

ROOT_URLCONF = 'HelpingHandServer.urls'
STATIC_URL = '/static/'
WSGI_APPLICATION = 'HelpingHandServer.wsgi.application'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATICFILE_DIRS = (
    os.path.join(BASE_DIR,'main/static/'),
    os.path.join(BASE_DIR,'page/static/'),
)

#Middleware classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#Context Processors
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "main.context_processors.loginForm",
    "main.context_processors.logoutForm",
    "main.context_processors.signupForm",
    "django.core.context_processors.request"
)
SECRET_KEY = 'g7k0bao*dl3ea)*($)+t%gc*0i&u*-0k4q+p+jz!(08s69&*au'

#Administrators
ADMINS = (
    ('John Carlyle', 'john.w.carlyle@gmail.com'),
    ('Jeremy Crowe', 'crowe.jb@gmail.com'),
    ('Morgan McDermott', 'morganmcdermott@gmail.com')
)
MANAGERS = ADMINS

INSTALLED_APPS = (
    'south',
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'page',)

#Template directories
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'main/templates'),
    os.path.join(BASE_DIR, 'page/templates')
)
DATABASES = { 'default': {
'ENGINE' : 'django.db.backends.sqlite3', 'NAME' : os.path.join(BASE_DIR, 'db.db')
} }
