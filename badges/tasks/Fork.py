import requests
from GitGaming import settings
from badges.req import req
from stats.models import APIStats
import time
from GitGaming.SECRET import GITHUB2, GITHUB1


def check(user, forks, **kwargs):
    """
        Check
    :param user:
    :param forks: Minimum forks required
    :param kwargs:
    :return: True/False if the badge is given
    """

    url = req['get_user_repos'].format(user, GITHUB1, GITHUB2)
    print url
    repos = requests.get(url)
    amount = 0
    for repo in repos.json():
        if settings.DEBUG:
            print 'Fork Badge checking - From cache: {}'.format(repos.from_cache)

        if repo['fork']:
            amount += 1

    if amount >= forks:
        return True
    return False
