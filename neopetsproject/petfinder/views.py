import os
import datetime
import requests
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import PetSearchForm
from .models import Pet

def index(request):
    updatePetfinderToken()
    context = {
        'pet_types': getAnimalTypes(),
        'genders': ['male', 'female'],
        'statuses': ['adoptable', 'adopted', 'found'],
    }
    return render(request, 'petfinder/index.html', context)

def search(request):
    updatePetfinderToken()
    url = os.getenv('PETFINDER_BASE_URL') + '/v2/animals'
    request_headers = {
        'Authorization': 'Bearer ' + os.getenv('PETFINDER_ACCESS_TOKEN')
    }
    url_params = {}
    for field in request.GET:
        if request.GET.getlist(field) and request.GET.getlist(field)[0]:
            url_params[field] = ','.join(request.GET.getlist(field))
    response = requests.get(url, params=url_params, headers=request_headers)
    response = json.loads(response.text)
    favorites = Pet.objects.all()
    favorites = [f.id for f in favorites]
    print(favorites)

    context = {
        'pet_types': getAnimalTypes(),
        'genders': ['male', 'female'],
        'statuses': ['adoptable', 'adopted', 'found'],
        'results': response,
        'favorites': []
    }
    return render(request, 'petfinder/search.html', context)

def addFavorite(request):
    if request.POST and request.is_ajax():
        updatePetfinderToken()
        # TODO: make api call to get animal info, curate data and insert into petfinder_pet table, gg.
        response = requests.get(os.getenv('PETFINDER_BASE_URL')+'/v2/animals/'+request.POST['id'], headers={'Authorization': 'Bearer ' + os.getenv('PETFINDER_ACCESS_TOKEN')})
        response = json.loads(response.text)

    return JsonResponse({'data': 'success'})

def deleteFavorite(request):
    if request.POST and request.is_ajax():
        print(request.POST)
        pass

    return JsonResponse("{'key': 'test'}")


# helpers
def updatePetfinderToken():
    # TODO: store time of last token fetch, if time delta from last taken to now() is > 3590 seconds, request another one
    url = os.getenv('PETFINDER_BASE_URL') + '/v2/oauth2/token'
    url_params = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('PETFINDER_API_KEY'),
        'client_secret': os.getenv('PETFINDER_API_SECRET')
    }
    response = requests.post(url, data=url_params)
    serializedText = json.loads(response.text)
    os.environ['PETFINDER_ACCESS_TOKEN'] = serializedText['access_token']

def getAnimalTypes():
    updatePetfinderToken()
    types_url = os.getenv('PETFINDER_BASE_URL') + '/v2/types'
    request_headers = {
        'Authorization': 'Bearer ' + os.getenv('PETFINDER_ACCESS_TOKEN')
    }
    response = requests.get(types_url, headers=request_headers)
    response = json.loads(response.text)

    return [t['name'] for t in response['types']]