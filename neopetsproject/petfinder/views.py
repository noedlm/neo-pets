import os
import datetime
import requests
import json

from django.shortcuts import render
from django.http import HttpResponse
from .forms import PetSearchForm

def index(request):
    updatePetfinderToken()
    context = {
        'pet_types': getAnimalTypes(),
        'genders': ['male', 'female'],
        'statuses': ['adoptable', 'adopted', 'found'],
    }
    return render(request, 'petfinder/index.html', context)

def search(request):
    print(request.GET)
    updatePetfinderToken()
    url = os.getenv('PETFINDER_BASE_URL') + '/v2/animals'
    request_headers = {
        'Authorization': 'Bearer ' + os.getenv('PETFINDER_ACCESS_TOKEN')
    }
    url_params = {
        'type': 'dog',
        'name': 'duke'
    }
    response = requests.get(url, params=url_params, headers=request_headers)
    response = json.loads(response.text)
    context = {
        'pet_types': getAnimalTypes(),
        'genders': ['male', 'female'],
        'statuses': ['adoptable', 'adopted', 'found'],
        'results': response
    }
    context.update(request.GET)
    print(response)
    return render(request, 'petfinder/index.html', context)


#helpers
def updatePetfinderToken():
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