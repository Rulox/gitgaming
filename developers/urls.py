from django.conf.urls import patterns, include, url
from views import DeveloperDetailView


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$', DeveloperDetailView.as_view(), name='user_detail'),

)

