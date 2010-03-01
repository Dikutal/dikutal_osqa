# encoding:utf-8
# Django settings for lanai project.
import os.path
import sys

SITE_ID = 1

ADMIN_MEDIA_PREFIX = '/forum/admin/media/'
SECRET_KEY = '$oo^&_m&qwbib=(_4m_n*zn-d=g#s0he5fx9xonnym#8p6yigm'
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'forum.modules.module_templates_loader',
    'forum.skins.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = [
    #'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.middleware.sqlprint.SqlPrintingMiddleware',
    'forum.middleware.anon_user.ConnectToSessionMessagesMiddleware',
    'forum.middleware.pagesize.QuestionsPageSizeMiddleware',
    'forum.middleware.cancel.CancelActionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'recaptcha_django.middleware.ReCaptchaMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'context.application_settings',
    #'django.core.context_processors.i18n',
    'forum.user_messages.context_processors.user_messages',#must be before auth
    'django.core.context_processors.auth', #this is required for admin
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),'forum','skins').replace('\\','/'),
)

#UPLOAD SETTINGS
FILE_UPLOAD_TEMP_DIR = os.path.join(os.path.dirname(__file__), 'tmp').replace('\\','/')
FILE_UPLOAD_HANDLERS = ("django.core.files.uploadhandler.MemoryFileUploadHandler",
 "django.core.files.uploadhandler.TemporaryFileUploadHandler",)
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
# for user upload
ALLOW_FILE_TYPES = ('.jpg', '.jpeg', '.gif', '.bmp', '.png', '.tiff')
# unit byte
ALLOW_MAX_FILE_SIZE = 1024 * 1024

# User settings
from settings_local import *

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'forum',
    #'django_authopenid',
    'debug_toolbar' ,
]

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',]

if USE_SPHINX_SEARCH:
    INSTALLED_APPS.append('djangosphinx')

if USE_FB_CONNECT:
    INSTALLED_APPS.append('fbconnect')

if DATABASE_ENGINE in ('postgresql_psycopg2', 'postgresql', ) and False:
    USE_PG_FTS = True
    INSTALLED_APPS.append('pgfulltext')
else:
    USE_PG_FTS = False

#load optional plugin module for external password login
if 'USE_EXTERNAL_LEGACY_LOGIN' in locals() and USE_EXTERNAL_LEGACY_LOGIN:
    INSTALLED_APPS.append(EXTERNAL_LEGACY_LOGIN_MODULE)

    if 'EXTERNAL_LEGACY_LOGIN_AUTHENTICATION_BACKEND' in locals():
        AUTHENTICATION_BACKENDS.append(EXTERNAL_LEGACY_LOGIN_AUTHENTICATION_BACKEND)
    if 'EXTERNAL_LEGACY_LOGIN_AUTHENTICATION_MIDDLEWARE' in locals():
        MIDDLEWARE_CLASSES.append(EXTERNAL_LEGACY_LOGIN_AUTHENTICATION_MIDDLEWARE)
    def LOAD_EXTERNAL_LOGIN_APP():
        return __import__(EXTERNAL_LEGACY_LOGIN_MODULE, [], [], ['api','forms','views'])
else:
    LOAD_EXTERNAL_LOGIN_APP = lambda: None
