from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

import csv
from pagination.settings import BUS_STATION_CSV
from pprint import pprint

def index(request):
    return redirect(reverse('bus_stations'))


CONTENT = [str(i) for i in range(1000)]


def bus_stations(request):
    bus_stations = list()
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stations.append(row)
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
