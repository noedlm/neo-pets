import os
import datetime
import requests
import json

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'pet_types': ['dog','cat','bird','rabbit'],
    }
    return render(request, 'petfinder/index.html', context)

def search(request):
    updatePetfinderToken()
    url = os.getenv('PETFINDER_BASE_URL') + '/v2/animals'
    request_headers = {
        'Authorization': 'Bearer ' + os.environ['PETFINDER_ACCESS_TOKEN']
    }
    url_params = {
        'type': 'dog'
    }

    response = requests.get(url, params=url_params, headers=request_headers)
    return HttpResponse(response.text)


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
