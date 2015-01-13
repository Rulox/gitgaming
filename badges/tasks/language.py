# https://api.github.com/repos/Rulox/LUNO/languages
from pygithub3 import Github

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
        :param kwargs:
        :return: True/False if badge is given or not
        """
        gh = Github(login=user)
        developer = gh.users.get(user) # Api call
        repos = gh.repos.get()
        print repos


        return