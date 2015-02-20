import requests
from GitGaming import settings
from badges.req import req
from stats.models import APIStats
import time


def check(user, bytes, language, **kwargs):
    """
    Check LanguageBadge
    :param user:  Developer
    :param bytes:  Bytes or Lines in a language
    :param language:  String with the name of the language
    :param kwargs: Optional dictionary
    :return: True/False if badge is given or not
    """
    # We won't use the PyGithub library for now, it has some issues with this request.
    url = req['get_user_repos'].format(user)
    repos = requests.get(url)

    for repo in repos.json():
        url = repo[u'languages_url']
        languages = requests.get(url)

        if settings.DEBUG:
            print 'Language Badge checking - From cache: {}'.format(languages.from_cache)

        if not languages.from_cache:
            now = time.strftime('%Y-%m-%d')
            api, created = APIStats.objects.get_or_create(date=now)
            api.inc_call()
            api.save()

        amount = 0

        for lang, size in languages.json().iteritems():
            if lang == language:
                amount += size
            if amount >= bytes:
                return True
    return False