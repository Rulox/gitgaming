from django.contrib import admin
from .models import FidelityBadge, LanguageBadge, ForkBadge

# Register your models here.
admin.site.register(FidelityBadge)
admin.site.register(LanguageBadge)
admin.site.register(ForkBadge)