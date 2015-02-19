from django import forms
from django.forms import ModelForm
from developers.models import Profile
from django.utils.translation import ugettext as _

class DeveloperProfileForm(ModelForm):
    header = forms.ImageField(required=False, widget=forms.FileInput, label=_('Change your header image and drag it!'))

    class Meta:
        model = Profile
        fields = ['header', 'header_cropping', 'bio', 'website',]