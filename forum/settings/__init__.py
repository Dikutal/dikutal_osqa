import os.path
from base import Setting, SettingSet
from forms import ImageFormWidget

from django.forms.widgets import Textarea
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as djsettings

OSQA_VERSION = Setting('OSQA_VERSION', "Development Version")
SETTINGS_PACK = Setting('SETTINGS_PACK', "default")
APP_URL = djsettings.APP_URL
FORUM_SCRIPT_ALIAS = djsettings.FORUM_SCRIPT_ALIAS


from basic import *
from email import *
from extkeys import *
from minrep import *
from repgain import *
from voting import *
from upload import *
from about import *
from faq import *
from form import *
from moderation import *
from users import *

BADGES_SET = SettingSet('badges', _('Badges config'), _("Configure badges on your OSQA site."), 500)

#__all__ = locals().keys()

