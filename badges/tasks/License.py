import requests
from GitGaming import settings
from badges.req import req
from stats.models import APIStats
import time
from GitGaming.SECRET import GITHUB2, GITHUB1
import json

def check(user, license, nrepos, **kwargs):
    """
    Check LicenseBadge
    :param user:  Developer
    :param license: license name
    :param nrepos:  license count in all repos
    :param kwargs: Optional dictionary
    :return: True/False if badge is given or not
    """

    url = req['get_user_repos'].format(user, GITHUB1, GITHUB2)
    headers = {"Accept": "application/vnd.github.drax-preview+json"}
    print url
    amount = {}
    repos = requests.get(url, headers=headers)
    for repo in repos.json():
        try:
            url = repo[u'license']
            print json.dumps(url, sort_keys=True,
                             indent=4, separators=(',', ': '))
        except:
            print 'dont exists'


        if settings.DEBUG:
            print 'License Badge checking - From cache: {}'.format(repos.from_cache)

        if not repos.from_cache:
            now = time.strftime('%Y-%m-%d')
            api, created = APIStats.objects.get_or_create(date=now)
            api.inc_call()
            api.save()
    #check the number of repos with license
    #return False
