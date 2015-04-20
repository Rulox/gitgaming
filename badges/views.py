from django.shortcuts import render, render_to_response
from .models import Badge, CustomBadge
from developers.models import Achievement
from django.utils.translation import ugettext as _
from django.template import RequestContext
from datetime import datetime
from django.utils import timezone

# Create your views here.


def grant_custom_badge(request, code):
    try:
        b = CustomBadge.objects.get(code=code)
        try:
            Achievement.objects.get(user=request.user.django_user, badge=b)
            return render_to_response('badges/custom_badge_error.html', {'msg': _('Yoy already have this badge!')},
                                      context_instance=RequestContext(request))
        except Achievement.DoesNotExist:
            now = timezone.now()
            if now <= b.expiration_date:
                a = Achievement(user=request.user.django_user, badge=b)
                a.save()
                return render_to_response('badges/custom_badge_error.html', {'msg': _('You have earned a new badge!')},
                                          context_instance=RequestContext(request))
            else:
                return render_to_response('badges/custom_badge_error.html',
                                          {'msg': _('This badge is no longer available.')},
                                          context_instance=RequestContext(request))
    except Badge.DoesNotExist:
        return render_to_response('badges/custom_badge_error.html',
                                  {'msg': _('There is no badge with this code. We are sorry!')},
                                  context_instance=RequestContext(request))