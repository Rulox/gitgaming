from django.utils import timezone

def check(date, **kwargs):
    now = timezone.now()
    if now < date:
        return True
    return False