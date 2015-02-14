from django.forms import ModelForm
from models import Profile


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('header', 'header_cropping', 'bio', 'website',)