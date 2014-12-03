from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView
from developers.models import Developer


class DeveloperDetailView(DetailView):
    model = Developer
    template_name = 'developers/developer_detail.html'
