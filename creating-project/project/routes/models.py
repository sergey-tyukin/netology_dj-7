from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_center(self):
        stations = Station.objects.filter(routes=self)

        sum_latitude = 0
        sum_longitude = 0

        for station in stations:
            sum_latitude +=station.latitude
            sum_longitude += station.longitude

        average_latitude = sum_latitude / stations.count()
        average_longitude = sum_longitude / stations.count()

        return {'y': average_latitude, 'x': average_longitude}


class Station(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    routes = models.ManyToManyField(Route, related_name='stations')
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def route_numbers(self):
        return Route.objects.filter(stations=self).count()
