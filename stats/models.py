from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class APIStats(models.Model):
    """
        API Usage stats.
        Number of GitHub API Calls each day
    """
    date = models.DateField(verbose_name=_('Day stats'), auto_now=True)
    calls_number = models.IntegerField(verbose_name=_('Number of API Calls'), default=0)

    def inc_call(self):
        self.calls_number += 1


class UserStats(models.Model):
    """
        User Stats.
        Number of New Users each day
    """
    date = models.DateField(verbose_name=_('Day stats'), auto_now=True)
    users = models.IntegerField(verbose_name=_("Number of New Users"), default=0)

    def inc_user(self):
        self.users += 1


class RepoStats(models.Model):
    """
        Repositories Stats.
        Number of repositories analyzed each day
    """
    date = models.DateField(verbose_name=_('Day stats'), auto_now=True)
    repos = models.IntegerField(verbose_name=_('Number of repositories'), default=0)