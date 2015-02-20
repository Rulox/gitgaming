from django import forms
from django.forms import ModelForm
from developers.models import Profile, Achievement
from django.utils.translation import ugettext as _

class DeveloperProfileForm(ModelForm):
    header = forms.ImageField(required=False, widget=forms.FileInput, label=_('Change your header image and crop it!'))
    header_cropping = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(DeveloperProfileForm, self).__init__(*args, **kwargs)
        achievements = Achievement.objects.filter(user=kwargs['instance'].dev_user)
        titles = [("", "No title")]
        for ach in achievements:
            titles.append((ach.badge.title, ach.badge.title))

        self.fields['title'] = forms.ChoiceField(required=False, label=_('Select your title'),
                                                  choices=titles)

    class Meta:
        model = Profile
        fields = ['header', 'header_cropping', 'bio', 'title', 'website',]