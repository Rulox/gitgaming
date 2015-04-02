from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.


class Skill(models.Model):
    """
        Each developer will have a maximum of top 5 Skills.
        Each skill is a different Programming Language. With this, we can
        have information about most well known languages of each developer

        Skill will be an Inline ForeignKey relationship with Profile

        Developer 1..1 Profile 1..n Skills (up to 5)

        Percentage % will be relative. Top language will be 100% and the rest 4
        will be calculated based on that max
    """
    profile = models.ForeignKey('developers.Profile', related_name='skill', blank=False, null=False)
    language = models.CharField(max_length=255, blank=True, null=True)
    bytes = models.IntegerField(default=0, blank=True, null=True, help_text=_('Total bytes in this language'))

    def __unicode__(self):
        return "{} -> {} from: {}".format(self.language, self.bytes, self.profile)