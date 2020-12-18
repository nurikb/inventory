"""
Django settings for inventoryengine project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vp8mbe3)hw(7-rtfg)0l0c3s(*lm!@ip%oo20^*eienbwt9q04'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'inventory',
    'crispy_forms',
    'bootstrap4',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inventoryengine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'inventoryengine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inventory',
        'HOST' : 'localhost',
        'USER' : 'postgres',
        'PASSWORD' : 'nstat',
        'PORT' : '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ru-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        # 'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
                'Youtube'
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'youtube'
        ]),
    }
}

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'apps.core.pagination.StandardResultsSetPagination'
# }


# upstream inventory_app_server {
#   # fail_timeout=0 means we always retry an upstream even if it failed
#   # to return a good HTTP response (in case the Unicorn master nukes a
#   # single worker for timing out).
#
#   server unix:/dj/app/inventoryengine/run/gunicorn.sock fail_timeout=0;
# }
#
# server {
#
#     listen   80;
#     server_name example.com;
#
#     client_max_body_size 4G;
#
#     access_log /dj/app/inventoryengine/logs/nginx-access.log;
#     error_log /dj/app/inventoryengine/logs/nginx-error.log;
#
#     location /static/ {
#         alias   /dj/app/inventoryengine/static/;
#     }
#
#     location /media/ {
#         alias   /dj/app/inventoryengine/media/;
#     }
#
#     location / {
#         # an HTTP header important enough to have its own Wikipedia entry:
#         #   http://en.wikipedia.org/wiki/X-Forwarded-For
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#
#         # enable this if and only if you use HTTPS, this helps Rack
#         # set the proper protocol for doing redirects:
#         # proxy_set_header X-Forwarded-Proto https;
#
#         # pass the Host: header from the client right along so redirects
#         # can be set properly within the Rack application
#         proxy_set_header Host $http_host;
#
#         # we don't want nginx trying to do something clever with
#         # redirects, we set the Host: header above already.
#         proxy_redirect off;
#
#         # set "proxy_buffering off" *only* for Rainbows! when doing
#         # Comet/long-poll stuff.  It's also safe to set if you're
#         # using only serving fast clients with Unicorn + nginx.
#         # Otherwise you _want_ nginx to buffer responses to slow
#         # clients, really.
#         # proxy_buffering off;
#
#
#     location / {
#         # an HTTP header important enough to have its own Wikipedia entry:
#         #   http://en.wikipedia.org/wiki/X-Forwarded-For
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#
#         # enable this if and only if you use HTTPS, this helps Rack
#         # set the proper protocol for doing redirects:
#         # proxy_set_header X-Forwarded-Proto https;
#
#         # pass the Host: header from the client right along so redirects
#         # can be set properly within the Rack application
#         proxy_set_header Host $http_host;
#
#         # we don't want nginx trying to do something clever with
#         # redirects, we set the Host: header above already.
#         proxy_redirect off;
#
#         # set "proxy_buffering off" *only* for Rainbows! when doing
#         # Comet/long-poll stuff.  It's also safe to set if you're
#         # using only serving fast clients with Unicorn + nginx.
#         # Otherwise you _want_ nginx to buffer responses to slow
#         # clients, really.
#         # proxy_buffering off;
#
#         # Try to serve static files from nginx, no point in making an
#         # *application* server like Unicorn/Rainbows! serve static files.
#         if (!-f $request_filename) {
#             proxy_pass http://127.0.0.1:8001;
#             break;
#         }
#     }
#
#     # Error pages
#     error_page 500 502 503 504 /500.html;
#     location = /500.html {
#         root /dj/app/inventoryengine/static/;
#     }
# }
#
