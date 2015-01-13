from django.contrib import admin
from .models import APIStats, UserStats, RepoStats
# Register your models here.

admin.site.register(APIStats)
admin.site.register(UserStats)
admin.site.register(RepoStats)