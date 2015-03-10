import re
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from developers.models import Developer, Achievement, Profile

# Create your views here.
from django.views.generic import TemplateView, FormView, UpdateView
from developers.models import Developer
from .forms import DeveloperProfileForm
import simplejson


class DeveloperView(TemplateView):

    model = Developer
    template_name = 'developers/developer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DeveloperView, self).get_context_data(**kwargs)
        try:
            developer = Developer.objects.get(githubuser=kwargs['user'])
            context['object'] = developer
            developer.update_data_async()
            #developer.check_badges()
            #developer.update_profile()
            context['badges'] = Achievement.objects.filter(user=developer).order_by('date')
            return context
        except ObjectDoesNotExist:
            raise Http404()


class DeveloperProfileEditView(UpdateView):
    template_name = 'developers/developer_edit.html'
    success_url = '.'
    form_class = DeveloperProfileForm

    def get_object(self, queryset=None):
        dev = Developer.objects.get(githubuser=self.request.user)
        return Profile.objects.get(dev_user=dev)

    #TODO def form valid


def get_users(request):
    """
    Returns a JSON Object with users. It is used for
    realtime search in Navbar.
    :param request: POST Request with user string
    :return: JSON with all the users
    """
    if request.is_ajax():
        search = request.GET['srsearch']
        regex = re.escape(search)
        print regex
        print search
        devs = Developer.objects.filter(githubuser__contains=regex)
        response = [{'user': x.githubuser} for x in devs]
        return HttpResponse(simplejson.dumps(response))
    else:
        return HttpResponseRedirect(reverse('home'))

