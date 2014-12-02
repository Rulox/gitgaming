from django.conf.urls import patterns, include, url
from django.contrib import admin
from portal.views import PortalView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GitGaming.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PortalView.as_view(), name='home'),
)


urlpatterns += i18n_patterns( """ Patterns for translation """

)