from django.contrib import admin
from .models import APIStats, UserStats
# Register your models here.

admin.site.register(APIStats)
admin.site.register(UserStats)