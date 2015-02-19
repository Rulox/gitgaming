from django.conf.urls import patterns, include, url
from views import DeveloperView, DeveloperProfileEditView


urlpatterns = patterns('',
    url(r'^(?P<user>\w+)/$', DeveloperView.as_view(), name='user_detail'),
)