# from django.conf import settings
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Developer(models.Model):
    """ Main User Class
        Every user on the platform will have the following
        information related when 'register' their GitHub User
        for the first time.
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='django_user')
    githubuser = models.CharField(verbose_name=_('GitHub User account'), max_length=255, null=False, blank=False)
    level = models.IntegerField(verbose_name=_('Current level'), null=True, blank=True, default=1)
    repos = models.IntegerField(null=True, blank=True)  # IDEA: You have X repositories in your inventory
    max_streak = models.IntegerField(null=True, blank=True)
    experience = models.DecimalField(null=True, blank=True, default=0.0, decimal_places=2, max_digits=4)
    title = models.CharField(null=True, blank=True, max_length=255)
    register_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)
    avatar = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.githubuser



class Profile(models.Model):
    """ Developer Game Profile
        Each user has a "Gaming profile". It will collect information about
        some skills so a
    """
    pass



def save_user(backend, user, response, *args, **kwargs):
    """
        When an user Login with GitHub, we create a Developer instance
        so we can have an associated Developer profile with that
        authenticated user
    """
    if backend.name == 'github':
        if not Developer.objects.get(user=user):
            developer = Developer()
            developer.githubuser = response['login']
            developer.avatar = response['avatar_url']
            developer.repos = response['public_repos']
            developer.user = user
            developer.save()