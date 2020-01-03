import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        Phone.objects.all().delete()

        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            phone_catalog = []
            for line in phone_reader:
                phone_catalog.append(line)

        for item in phone_catalog:
            Phone.objects.create(name=item[1], price=float(item[3]), image=item[2],
                                 release_date=datetime.strptime(item[4], '%Y-%m-%d'),
                                 lte_exists=bool(item[5]))
