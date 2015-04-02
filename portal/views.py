from django.shortcuts import render
from django.views.generic import TemplateView
from developers.models import Developer
from django.core.paginator import Paginator
# Create your views here.

class PortalView(TemplateView):
    template_name = 'portal/index.html'


class RankingView(TemplateView):
    template_name = 'portal/ranking.html'

    def get_context_data(self, **kwargs):
        context = super(RankingView, self).get_context_data(**kwargs)
        devs = Developer.objects.all()
        context['developers'] = devs

        return context
