from django.shortcuts import render, get_object_or_404
from developers.models import Developer

# Create your views here.
from django.views.generic import TemplateView
from developers.models import Developer


class DeveloperView(TemplateView):

    model = Developer
    template_name = 'developers/developer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DeveloperView, self).get_context_data(**kwargs)
        context['object'] = Developer.objects.get(githubuser=kwargs['user'])
        return context
