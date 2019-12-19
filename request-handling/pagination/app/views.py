from csv import DictReader
from urllib.parse import urlencode

from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))

def bus_stations(request):
    count_per_page = 10

    with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as csvfile:
        reader = DictReader(csvfile)
        data = [dict(item) for item in reader]

    paginator = Paginator(data, count_per_page)

    current_page = int(request.GET.get('page', 1))
    if current_page < 1:
        current_page = 1
    if current_page > paginator.num_pages:
        current_page = paginator.num_pages

    page = paginator.get_page(current_page)

    if page.has_previous():
        prev_page_url = reverse('bus_stations') + '?' + \
                        urlencode({'page': page.previous_page_number()})
    else:
        prev_page_url = None

    if page.has_next():
        next_page_url = reverse('bus_stations') + '?' + \
                        urlencode({'page': page.next_page_number()})
    else:
        next_page_url = None

    return render_to_response('index.html', context={
        'bus_stations': data[(current_page - 1) * 10: current_page * 10],
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
