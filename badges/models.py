from django.db import models
from django.utils.translation import ugettext as _
import pkgutil


# Create your models here.
""" Deprecated
modules = pkgutil.iter_modules(path=["badges/tasks"])
a = []
for loader, mod_name, ispkg in modules:
    a.append(str(mod_name))

METHOD_CHOICES = [(name, name) for name in a]
"""

class Badge(models.Model):
    """ Parent class
        Base Badge.
    """
    name = models.CharField(blank=False, null=False, max_length=255)
    title = models.CharField(verbose_name=_('Title given with badge (if proceed)'), blank=True,
                             null=True, max_length=255)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='badges', blank=False, null=False)
    date = models.DateTimeField(verbose_name='Creation date', name="date", auto_now=True)
    experience = models.DecimalField(verbose_name=_('Experience gained with this badge'),
                                     default=5.0, decimal_places=2, max_digits=4)

    def __unicode__(self):
        return "{}".format(self.name)

    @property
    def is_language(self):
        try:
            return self.languagebadge
        except LanguageBadge.DoesNotExist:
            return False


    @property
    def is_fidelity(self):
        try:
            return self.fidelitybadge
        except FidelityBadge.DoesNotExist:
            return False

    @property
    def is_fork(self):
        try:
            return self.forkbadge
        except:
            return False


class FidelityBadge(Badge):
    """ Fidelity Badge
        These kinds of badges are granted when users create an account
        in certain periods, i.e. during the Beta.

        It has the fields of the Parent and these:
    """
    end_date = models.DateTimeField(verbose_name='Deadtime for the Badge', blank=False, null=False)

    def __unicode__(self):
        return "{} until {}".format(self.name, self.end_date)



class LanguageBadge(Badge):
    """ Language Bytes count Badge

        These kind of badges are granted when users reach X bytes of code
        in a language. Parameters are Number of bytes and Language.
    """
    bytes = models.IntegerField(verbose_name='Number of bytes or lines', blank=False, null=False)
    language = models.CharField(verbose_name='Language. (ie: Ruby, Python, etc)', max_length=255, blank=False, null=False)

    def __unicode__(self):
        return "{} badge from {} bytes of code".format(self.name, self.bytes)


class ForkBadge(Badge):
    """ ForkBadge

        These kinds of badges are granted when user has X number of repos forked from
        other user's repos. We want to make a comparision between "Fork" and "Force" from Star Wars
        to make these badges funnier.

        i.e. 'May the Fork be with you'
    """
    forks = models.IntegerField(verbose_name='Number fo minimum repos forked', blank=False, null=False)


class SuperStarBadge(Badge):
    pass

class LevelBadge(Badge):
    """
        Badge given when you reach certain levels.
    """

    level = models.IntegerField(verbose_name='Level', blank=False, null=False)