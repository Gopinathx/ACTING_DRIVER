from django.shortcuts import render
from .models import Driver

def driver_list(request):
    city = request.GET.get('city', '')
    transmission = request.GET.get('transmission', '')

    drivers = Driver.objects.prefetch_related('pricing').filter(is_available=True)

    if city:
        drivers = drivers.filter(city__iexact=city)
    if transmission:
        drivers = drivers.filter(transmission_type=transmission)

    return render(request, 'drivers/driver_list.html', {
        'drivers': drivers,
        'selected_city': city,
        'selected_transmission': transmission,
    })