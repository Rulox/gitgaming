from django.core.management.base import BaseCommand
from developers.models import Developer


class Command(BaseCommand):
    help = "Update"

    def handle(self, *args, **options):
        for developer in Developer.objects.all():
            developer.update_data_async()