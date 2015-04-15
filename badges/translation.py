from .models import Badge
from modeltranslation.translator import translator, TranslationOptions


class BadgeTranslationOptions(TranslationOptions):
    fields = ('description', )

translator.register(Badge, BadgeTranslationOptions)