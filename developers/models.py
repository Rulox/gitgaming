# from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from django.db import models


# Create your models here.
class Developer(models.Model):
    """ Main User Class
        Every user on the platform will have the following
        information related when 'register' their GitHub User
        for the first time.
    """

    # TODO relation with Django users in order to implement authentication
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='django_user')
    # supervisor = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='supervisor_of')
    githubuser = models.CharField(max_length=255, null=False, blank=False)
    level = models.IntegerField(null=True, blank=True, default=1)
    repos = models.IntegerField(null=True, blank=True)  # IDEA: You have X repositories in your inventory
    maxstreak = models.IntegerField(null=True, blank=True)
    experience = models.DecimalField(null=True, blank=True, default=0.0, decimal_places=2, max_digits=4)
    title = models.CharField(null=True, blank=True, max_length=255)
    registerdate = models.DateTimeField(auto_now=True)
    lastupdate = models.DateTimeField(auto_now=True)
    avatar = models.URLField(null=True, blank=True)


    def __unicode__(self):
        return self.githubuser


""" pre_save Signal """
@receiver(pre_save, sender=Developer)
def my_callback(sender, instance, *args, **kwargs):
    """
    This pre_save signal is sent before saving the data in the database.
    We will collect repos (number of public repositories) and maxstreak
    before saving the user in the Database
    """
    instance.title = _("Apprentice")