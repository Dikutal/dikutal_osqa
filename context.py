from django.conf import settings
def application_settings(context):
    my_settings = {
        'APP_TITLE' : settings.APP_TITLE,
        'APP_SHORT_NAME' : settings.APP_SHORT_NAME,
        'APP_URL'   : settings.APP_URL,
        'APP_KEYWORDS' : settings.APP_KEYWORDS,
        'APP_DESCRIPTION' : settings.APP_DESCRIPTION,
        'APP_INTRO' : settings.APP_INTRO,
        'EMAIL_VALIDATION': settings.EMAIL_VALIDATION,
        'LANGUAGE_CODE': settings.LANGUAGE_CODE,
        'GOOGLE_SITEMAP_CODE':settings.GOOGLE_SITEMAP_CODE,
        'GOOGLE_ANALYTICS_KEY':settings.GOOGLE_ANALYTICS_KEY,
        'BOOKS_ON':settings.BOOKS_ON,
        'WIKI_ON':settings.WIKI_ON,
        'USE_EXTERNAL_LEGACY_LOGIN':settings.USE_EXTERNAL_LEGACY_LOGIN,
        'RESOURCE_REVISION':settings.RESOURCE_REVISION,
        'USE_SPHINX_SEARCH':settings.USE_SPHINX_SEARCH,
        'OSQA_SKIN':settings.OSQA_DEFAULT_SKIN,
        }
    return {'settings':my_settings}

def auth_processor(request):
    """
    Returns context variables required by apps that use Django's authentication
    system.

    If there is no 'user' attribute in the request, uses AnonymousUser (from
    django.contrib.auth).
    """
    if hasattr(request, 'user'):
        user = request.user
        if user.is_authenticated():
            messages = user.message_set.all()
        else:
            messages = None
    else:
        from django.contrib.auth.models import AnonymousUser
        user = AnonymousUser()
        messages = None

    from django.core.context_processors import PermWrapper
    return {
        'user': user,
        'messages': messages,
        'perms': PermWrapper(user),
    }
