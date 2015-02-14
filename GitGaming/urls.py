from django.conf.urls import patterns, include, url
from django.contrib import admin
import developers
from portal.views import PortalView
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from GitGaming import settings


admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'GitGaming.views.home', name='home'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), #DEBUG
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^auth/', 'githubauth.views.Home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)


urlpatterns += i18n_patterns('',
    url(r'^user/', include('developers.urls')),
    url(r'^$', PortalView.as_view(), name='home'),

)