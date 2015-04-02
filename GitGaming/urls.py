from django import template
from django.conf.urls import patterns, include, url
from django.contrib import admin
import developers
from django.shortcuts import render_to_response
from portal.views import PortalView, RankingView, BadgeListView
from developers.views import DeveloperProfileEditView
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from GitGaming import settings
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'GitGaming.views.home', name='home'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), #DEBUG
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^auth/', 'githubauth.views.Home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    #zinnia blog
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),

    #Language config
    url(r'^i18n/', include('django.conf.urls.i18n')),
)


urlpatterns += i18n_patterns('',
    url(r'^get_users_ajax/$', "developers.views.get_users", name='get_users_ajax'),
    url(r'^user/', include('developers.urls')),
    url(r'^edit/$', login_required(DeveloperProfileEditView.as_view()), name='user_edit'),
    url(r'^ranking$', RankingView.as_view(), name='ranking'),
    url(r'^badges$', BadgeListView.as_view(), name='badge_list'),
    url(r'^$', PortalView.as_view(), name='home'),

)



