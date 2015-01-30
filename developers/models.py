# from django.conf import settings
from audioop import alaw2lin
from datetime import time
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth import get_user_model
from badges.models import Badge
from stats.models import APIStats, UserStats
from badges.tasks import Language
import time

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
    badge = models.ManyToManyField(Badge, through='Achievement')

    def __unicode__(self):
        return self.githubuser


    def check_badges(self):
        for badge in Badge.objects.all():
            if badge not in Achievement.objects.filter(user=self.user, badge=badge):
                # Check all types of badges
                if badge.is_language:
                    l = Language.Language()
                    #print l.check(self.githubuser, lang.bytes, lang.language)





class Achievement(models.Model):
    """
        Achievement class. This model is used to connect Users with Badges. It will have information
        about each badge earned by every user and the date of the achievement.
    """
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(Developer, related_name='developer')
    badge = models.ForeignKey(Badge, related_name='badge')

class Profile(models.Model):
    """ Developer Game Profile
        Each user has a "Gaming profile". It will collect information about
        some basic skills. It's the same as "INTELECT" or "STAMINA" in some videogames.

        It will store also the image that every user can upload to their header profile page. Just like Facebook, etc.
    """
    dev_user = models.OneToOneField(Developer, related_name='profile')
    header = models.FileField(upload_to='/headers/', blank=True, null=True)

    def __unicode__(self):
        return 'Profile of: {}'.format(self.developer)


def save_user(backend, user, response, *args, **kwargs):
    """
        When an user Login with GitHub, we create a Developer instance
        so we can have an associated Developer profile with that
        authenticated user
    """
    if backend.name == 'github':
        try:
            dev = Developer.objects.get(user=user)
            # If exists, we check for any new update in the repos. Check all the badges
            # FIXME In the future, this function will be called using Celery
            dev.check_badges()
            return
        except ObjectDoesNotExist:
            if settings.DEBUG:
                print "Creating new user {}".format(user)

            # Analytics stuff
            now = time.strftime('%Y-%m-%d')
            u, created = UserStats.objects.get_or_create(date=now)
            u.inc_user()
            u.save()

            api, created = APIStats.objects.get_or_create(date=now)
            api.inc_call()
            api.save()

            # Create user
            developer = Developer()
            developer.githubuser = response['login']
            developer.avatar = response['avatar_url']
            developer.repos = response['public_repos']
            developer.user = user
            developer.save()