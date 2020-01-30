import csv

from django.core.management.base import BaseCommand

from routes.models import Station, Route

class Command(BaseCommand):
    help = 'Load data into DB from file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Путь к файлу для загрузки')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                routes = row['RouteNumbers'].split(';')
                station = Station.objects.create(latitude=float(row['Latitude_WGS84']),
                                                 longitude=float(row['Longitude_WGS84']),
                                                 name=row['Name'])
                for route_name in routes:
                    route = Route.objects.update_or_create(name=route_name,
                                                           defaults={
                                                               'name': route_name})
                    station.routes.add(route[0])
