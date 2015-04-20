from django.contrib import admin
from .models import FidelityBadge, LanguageBadge, ForkBadge, LicenseBadge, CustomBadge

# Register your models here.
admin.site.register(CustomBadge)
admin.site.register(FidelityBadge)
admin.site.register(LanguageBadge)
admin.site.register(ForkBadge)
admin.site.register(LicenseBadge)
