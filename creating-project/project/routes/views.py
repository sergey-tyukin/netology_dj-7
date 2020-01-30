from django.shortcuts import render
from django.views import View

from .models import Route, Station


class RoutesView(View):

    def get(self, request):
        route_name = request.GET.get('route')

        if route_name:
            route = Route.objects.filter(name=route_name).first()
            stations = Station.objects.filter(routes=route)
        else:
            stations = []

        context = {'routes': Route.objects.all(),
                   'stations': stations}
        return render(request, 'routes/stations.html', context)
