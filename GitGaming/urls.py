from django.conf.urls import patterns, include, url
from django.contrib import admin
from portal.views import PortalView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GitGaming.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', PortalView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
