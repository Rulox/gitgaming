from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from developers.models import Developer
from badges.models import Badge
from django.core.paginator import Paginator
# Create your views here.

class PortalView(TemplateView):
    template_name = 'portal/index.html'

    def get_context_data(self, **kwargs):
        context = super(PortalView, self).get_context_data(**kwargs)
        context['last_badges'] = Badge.objects.all().order_by('-date')[:3]
        return context


class RankingView(TemplateView):
    template_name = 'portal/ranking.html'

    def get_context_data(self, **kwargs):
        context = super(RankingView, self).get_context_data(**kwargs)
        devs = Developer.objects.all().order_by('-points')
        context['developers'] = devs

        return context

class BadgeListView(ListView):
    model = Badge
    template_name = 'portal/badge_listview.html'
