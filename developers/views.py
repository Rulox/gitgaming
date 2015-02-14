from django.shortcuts import render, get_object_or_404
from developers.models import Developer, Achievement, Profile
from forms import ProfileEditForm


# Create your views here.
from django.views.generic import TemplateView, FormView, UpdateView
from developers.models import Developer


class DeveloperView(TemplateView):

    model = Developer
    template_name = 'developers/developer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DeveloperView, self).get_context_data(**kwargs)
        developer = Developer.objects.get(githubuser=kwargs['user'])
        context['object'] = developer
        # FIXME In the future, this function will be called using Celery
        developer.check_badges()
        developer.update_profile()
        context['badges'] = Achievement.objects.filter(user=developer).order_by('-date')
        return context


class DeveloperProfileEditView(UpdateView):

    template_name = 'developers/developer_edit.html'
    success_url = '/'

    def get_object(self):
        dev = Developer.objects.get(githubuser=self.request.user)
        return Profile.objects.get(dev_user=dev)




