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
from badges.tasks import Language, Fidelity
from badges.req import req
import time
import requests
from image_cropping import ImageRatioField

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
    repos = models.IntegerField(null=True, blank=True)
    max_streak = models.IntegerField(null=True, blank=True)
    experience = models.DecimalField(null=True, blank=True, default=0.0, decimal_places=2, max_digits=4)
    register_date = models.DateTimeField(auto_now=True)  # FIXME Deprecated. Migration to delete attr
    last_update = models.DateTimeField(auto_now=True)
    avatar = models.URLField(null=True, blank=True)
    badge = models.ManyToManyField(Badge, through='Achievement')

    def __unicode__(self):
        return self.githubuser

    def update_profile(self):
        """
            Update Developer Profile and basic information
        """
        profile, created = Profile.objects.get_or_create(dev_user=self)

        # User -------
        url = req['get_user_info'].format(self.githubuser)
        info = requests.get(url)


        if not info.from_cache:
            now = time.strftime('%Y-%m-%d')
            api, created = APIStats.objects.get_or_create(date=now)
            api.inc_call()
            api.save()

        info = info.json()
        profile.followers = info[u'followers']
        profile.following = info[u'following']
        self.repos = info[u'public_repos']
        self.save()

        # Repositories
        url = req['get_user_repos'].format(self.githubuser)
        repos = requests.get(url)

        if not repos.from_cache:
            now = time.strftime('%Y-%m-%d')
            api, created = APIStats.objects.get_or_create(date=now)
            api.inc_call()
            api.save()

        stars = 0
        forks = 0
        solver = 0

        for repo in repos.json():
            stars += int(repo[u'stargazers_count'])
            forks += int(repo[u'forks_count'])
            solver += int(repo[u'open_issues_count'])

        profile.stars = stars
        profile.forks = forks
        profile.solver = solver
        profile.save()


    def grant_badge(self, badge):
        """
            Update Developer Profile and add achievement for a given badge
        """
        a = Achievement()
        a.user = self
        a.badge = badge
        a.save()
        self.experience += badge.experience
        self.save()
        # TODO Check experience and increase level if proceed

    def check_badges(self):
        """
            With this function, we check over all the badges still not given to a user. If the Developer
            has the
        """

        for badge in Badge.objects.all():
            if not Achievement.objects.filter(user=self, badge=badge):
                if settings.DEBUG:
                    print 'Checking badge: {}'.format(badge)
                # Check all types of badges
                if badge.is_language:
                    b = badge.is_language
                    l = Language
                    if l.check(self.githubuser, b.bytes, b.language):
                        self.grant_badge(b)
                if badge.is_fidelity:
                    b = badge.is_fidelity
                    f = Fidelity
                    if f.check(b.end_date):
                        self.grant_badge(b)


class Achievement(models.Model):
    """
        Achievement class. This model is used to connect Users with Badges. It will have information
        about each badge earned by every user and the date of the achievement.
    """
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(Developer, related_name='developer')
    badge = models.ForeignKey(Badge, related_name='badge')

    def __unicode__(self):
        return 'Achievement {} for user {}'.format(self.badge, self.user)


class Profile(models.Model):
    """ Developer Game Profile
        Each user has a "Gaming profile". It will collect information about
        some basic skills. It's the same as "INTELECT" or "STAMINA" in some videogames.

        It will store also the image that every user can upload to their header profile page. Just like Facebook, etc.
    """
    dev_user = models.OneToOneField(Developer, related_name='profile')
    header = models.ImageField(upload_to='headers', blank=True, null=True)
    header_cropping = ImageRatioField('header', '1170x300')
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    title = models.CharField(null=True, blank=True, max_length=255)
    followers = models.IntegerField(blank=True, null=True, default=0)  # n of followers
    following = models.IntegerField(blank=True, null=True, default=0)  # n of following users
    solver = models.IntegerField(blank=True, null=True, default=0)     # n of open issues in all repos
    stars = models.IntegerField(blank=True, null=True, default=0)      # n of stars in all repos
    forks = models.IntegerField(blank=True, null=True, default=0)      # n of forks in all repos


    def __unicode__(self):
        return 'Profile of: {}'.format(self.dev_user)


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