import csv

from django.utils.text import slugify
from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('work_with_database/phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for item in phones:
            Phone.objects.create(
                id=item['id'],
                name=item['name'],
                price=item['price'],
                image=item['image'],
                release_date=item['release_date'],
                lte_exists=item['lte_exists'],
                slug=slugify(item['name']))
            Phone.save()
