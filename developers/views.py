from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from developers.models import Developer, Achievement, Profile

# Create your views here.
from django.views.generic import TemplateView, FormView, UpdateView
from developers.models import Developer
from .forms import DeveloperProfileForm

class DeveloperView(TemplateView):

    model = Developer
    template_name = 'developers/developer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DeveloperView, self).get_context_data(**kwargs)
        developer = Developer.objects.get(githubuser=kwargs['user'])
        context['object'] = developer
        developer.update_data_async()
        context['badges'] = Achievement.objects.filter(user=developer).order_by('-date')
        return context


class DeveloperProfileEditView(UpdateView):
    template_name = 'developers/developer_edit.html'
    success_url = '.'
    form_class = DeveloperProfileForm

    def get_object(self):
        dev = Developer.objects.get(githubuser=self.request.user)
        return Profile.objects.get(dev_user=dev)

    #TODO def form valid




