from django.conf.urls import patterns, include, url
from views import DeveloperView, DeveloperProfileEditView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^(?P<user>\w+)/$', DeveloperView.as_view(), name='user_detail'),
    url(r'^(?P<user>\w+)/edit/$', login_required(DeveloperProfileEditView.as_view()), name='user_edit'),
)