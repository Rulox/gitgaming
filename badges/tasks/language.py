import requests
from GitGaming import settings
from badges.req import req

# FIXME
import requests_cache
requests_cache.install_cache('test_cache', backend='sqlite', expire_after=300)

class Language:
    """
        With this class, we can check, for each Developer, if he has reached certain
        amount of lines/bytes in each programming language.
    """
    def __init__(self):
        return

    def __unicode__(self):
        return "Language Badge"

    def check(self, user, bytes, language, **kwargs):
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
                print 'From cache: {}'.format(languages.from_cache)

            amount = 0

            for lang, size in languages.json().iteritems():
                if lang == language:
                    amount += size
                if amount >= bytes:
                    return True
        return False