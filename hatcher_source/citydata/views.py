from django.shortcuts import render
from django.http import JsonResponse
from citydata.models import CityState

def search_city(request):
    query = request.GET.get('term', '')  # Get the search term from the request
    cities = CityState.objects.filter(city__istartswith=query).values_list('city','state')[:9]  # Limit to 10 results
    return JsonResponse(list(cities), safe=False)  # Return the data as JSON
