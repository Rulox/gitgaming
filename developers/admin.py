from django.contrib import admin
from models import Developer, Achievement, Profile
from image_cropping import ImageCroppingMixin
from skills.models import Skill
# Register your models here.

class SkillInline(admin.TabularInline):
    model = Skill

class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [
        SkillInline,
    ]

admin.site.register(Developer)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Achievement)
