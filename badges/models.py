from django.db import models
import tasks

# Create your models here.
"""
    Each badge has to have a method associated. With this method
    we can check if an user has the requirements to earn the badge.

    We have to pass, for each badge, method number, and parameters in
    a dictionary. Note that tasks are coded in "method" module.
"""
#FIXME esto no va
METHOD_CHOICES = [(nombre, nombre) for nombre in dir(tasks)]  # for method in dir(tasks)...

class Badge(models.Model):
    """ Parent class
        Base Badge.
    """
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=False, null=False)
    image = models.FileField(upload_to="/badges/", blank=False, null=False)
    date = models.DateTimeField(verbose_name="Date of achievement", name="date", auto_now=True)
    method = models.CharField(choices=METHOD_CHOICES, blank=False, null=False, max_length=512, default=METHOD_CHOICES[0])

    class Meta:
        abstract = True


class FidelityBadge(Badge):
    """ Fidelity Badge
        These kinds of badges are granted when users create an account
        in certain periods, i.e. during the Beta.

        It has the fields of the Parent and these:
    """
    endDate = models.DateTimeField(verbose_name="Deadtime for the Badge", blank=False, null=False)


class LanguageBadge(Badge):
    """ Language Bytes count Badge

        These kind of badges are granted when users reach X bytes of code
        in a language. Parameters are Number of bytes and Language.
    """
    bytes = models.IntegerField(verbose_name="Number of bytes", blank=False, null=False)
    language = models.CharField(verbose_name="Language. (ie: Ruby, Python, etc)", max_length=255, blank=False, null=False)