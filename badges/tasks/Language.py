import requests
from GitGaming import settings
from badges.req import req
from stats.models import APIStats
import time
from GitGaming.SECRET import GITHUB2, GITHUB1


def check(user, bytes, language, **kwargs):
    """
    Check LanguageBadge
    :param user:  Developer
    :param bytes:  Bytes or Lines in a language
    :param language:  String with the name of the language
    :param kwargs: Optional dictionary
    :return: True/False if badge is given or not
    """

    url = req['get_user_repos'].format(user, GITHUB1, GITHUB2)
    print url
    repos = requests.get(url)

    for repo in repos.json():
        url = repo[u'languages_url']
        url += "?client_id={}&client_secret={}".format(GITHUB1, GITHUB2)
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