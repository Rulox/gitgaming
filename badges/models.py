from django.db import models
from django.utils.translation import ugettext as _
import pkgutil


# Create your models here.
"""
    Each badge has to have a method associated. With this method
    we can check if an user has the requirements to earn the badge.

    We have to pass, for each badge, method number, and parameters in
    a dictionary. Note that tasks are coded in "method" module.
"""
modules = pkgutil.iter_modules(path=["badges/tasks"])
a = []
for loader, mod_name, ispkg in modules:
    a.append(str(mod_name))

METHOD_CHOICES = [(name, name) for name in a]


class Badge(models.Model):
    """ Parent class
        Base Badge.
    """
    name = models.CharField(blank=False, null=False, max_length=255)
    title = models.CharField(verbose_name=_('Title given with badge (if proceed)'), blank=True,
                             null=True, max_length=255)
    description = models.TextField(blank=False, null=False)
    image = models.FileField(upload_to='badges', blank=False, null=False)
    date = models.DateTimeField(verbose_name='Creation date', name="date", auto_now=True)
    experience = models.DecimalField(verbose_name=_('Experience gained with this badge'),
                                     default=5.0, decimal_places=2, max_digits=4)
    method = models.CharField(choices=METHOD_CHOICES, blank=False, null=False,
                              max_length=512,
                              default=METHOD_CHOICES[0])

    def __unicode__(self):
        return "{}".format(self.name)

class FidelityBadge(Badge):
    """ Fidelity Badge
        These kinds of badges are granted when users create an account
        in certain periods, i.e. during the Beta.

        It has the fields of the Parent and these:
    """
    end_date = models.DateTimeField(verbose_name='Deadtime for the Badge', blank=False, null=False)

    def __unicode__(self):
        return "{} until {}".format(self.name, self.end_date)

    @staticmethod
    def is_fidelity():
        return True

class LanguageBadge(Badge):
    """ Language Bytes count Badge

        These kind of badges are granted when users reach X bytes of code
        in a language. Parameters are Number of bytes and Language.
    """
    bytes = models.IntegerField(verbose_name='Number of bytes or lines', blank=False, null=False)
    language = models.CharField(verbose_name='Language. (ie: Ruby, Python, etc)', max_length=255, blank=False, null=False)

    def __unicode__(self):
        return "{} badge from {} bytes of code".format(self.name, self.bytes)

    @staticmethod
    def is_language():
        return True

class LevelBadge(Badge):
    """
        Badge given when you reach certain levels.
    """

    level = models.IntegerField(verbose_name='Level', blank=False, null=False)