from django.conf.urls.defaults import *
from django.utils.translation import ugettext as _
from django.conf import settings

urlpatterns = patterns('',
    (r'^%s' % settings.FORUM_SCRIPT_ALIAS, include('forum.urls')),
)

