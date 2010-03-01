# encoding:utf-8
import os.path
from django.utils.translation import ugettext as _

def check_local_setting(name, value):
    local_vars = locals()
    if name in local_vars and local_vars[name] == value:
        return True
    else:
        return False

SITE_SRC_ROOT = os.path.dirname(__file__)
LOG_FILENAME = 'django.osqa.log'

#for logging
import logging
logging.basicConfig(
    filename=os.path.join(SITE_SRC_ROOT, 'log', LOG_FILENAME),
    level=logging.DEBUG,
    format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
)

#ADMINS and MANAGERS
ADMINS = (('Forum Admin', 'forum@example.com'),)
MANAGERS = ADMINS

#DEBUG SETTINGS
DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

DATABASE_NAME = 'robofaqs'             # Or path to database file if using sqlite3.
DATABASE_USER = 'postgres'               # Not used with sqlite3.
DATABASE_PASSWORD = ''               # Not used with sqlite3.
DATABASE_ENGINE = 'postgresql_psycopg2'  #mysql, etc
DATABASE_HOST = '192.168.1.76'
DATABASE_PORT = ''

#Moved from settings.py for better organization. (please check it up to clean up settings.py)

#email server settings
SERVER_EMAIL = ''
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[OSQA] '
EMAIL_HOST='osqa.net'
EMAIL_PORT='25'
EMAIL_USE_TLS=False

#LOCALIZATIONS
TIME_ZONE = 'America/New_York'

###########################
#
#   this will allow running your forum with url like http://site.com/forum
#
#   FORUM_SCRIPT_ALIAS = 'forum/'
#
FORUM_SCRIPT_ALIAS = '' #no leading slash, default = '' empty string


#OTHER SETTINGS
APP_TITLE = u'OSQA: Open Source Q&A Forum'
APP_SHORT_NAME = u'OSQA'
APP_KEYWORDS = u'OSQA,CNPROG,forum,community'
APP_DESCRIPTION = u'Ask and answer questions.'
APP_INTRO = u'<p>Ask and answer questions, make the world better!</p>'
APP_COPYRIGHT = 'Copyright OSQA, 2009. Some rights reserved under creative commons license.'
LOGIN_URL = '/%s%s%s' % (FORUM_SCRIPT_ALIAS,'account/','signin/')
GREETING_URL = LOGIN_URL #may be url of "faq" page or "about", etc

USE_I18N = True
LANGUAGE_CODE = 'en'
EMAIL_VALIDATION = 'off' #string - on|off
MIN_USERNAME_LENGTH = 1
EMAIL_UNIQUE = False
APP_URL = 'http://osqa.net' #used by email notif system and RSS
GOOGLE_SITEMAP_CODE = ''
GOOGLE_ANALYTICS_KEY = ''
BOOKS_ON = False
WIKI_ON = True
USE_EXTERNAL_LEGACY_LOGIN = False
EXTERNAL_LEGACY_LOGIN_HOST = 'login.osqa.net'
EXTERNAL_LEGACY_LOGIN_PORT = 80
EXTERNAL_LEGACY_LOGIN_PROVIDER_NAME = '<span class="orange">OSQA</span>'
FEEDBACK_SITE_URL = None #None or url
EDITABLE_SCREEN_NAME = False #True or False - can user change screen name?

DJANGO_VERSION = 1.1
RESOURCE_REVISION=4

USE_SPHINX_SEARCH = False #if True all SPHINX_* settings are required
#also sphinx search engine and djangosphinxs app must be installed
#sample sphinx configuration file is /sphinx/sphinx.conf
SPHINX_API_VERSION = 0x113 #refer to djangosphinx documentation
SPHINX_SEARCH_INDICES=('osqa',) #a tuple of index names remember about a comma after the
#last item, especially if you have just one :)
SPHINX_SERVER='localhost'
SPHINX_PORT=3312

#please get these at recaptcha.net
RECAPTCHA_PRIVATE_KEY='...'
RECAPTCHA_PUBLIC_KEY='...'
OSQA_DEFAULT_SKIN = 'default'

#Facebook settings
USE_FB_CONNECT=False
FB_API_KEY='' #your api key from facebook
FB_SECRET='' #your application secret
