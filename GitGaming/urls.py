from django.conf.urls import patterns, include, url
from django.contrib import admin
from portal.views import PortalView
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GitGaming.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^auth/', 'githubauth.views.Home', name='home'),
    url(r'^$', PortalView.as_view(), name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

)


urlpatterns += i18n_patterns(
""" Patterns for translation """
)