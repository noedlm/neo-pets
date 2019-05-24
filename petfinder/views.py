import os
import datetime
import requests
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pet

def index(request):
    updatePetfinderToken()
    context = {
        'pet_types': getAnimalTypes(),
        'genders': ['male', 'female'],
        'statuses': ['adoptable', 'adopted', 'found']
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
    favorites = [f.animal_id for f in favorites]

    context = {
        'pet_types': getAnimalTypes(),
        'genders': ['male', 'female'],
        'statuses': ['adoptable', 'adopted', 'found'],
        'results': response,
        'favorites': favorites
    }
    return render(request, 'petfinder/search.html', context)

def addFavorite(request):
    if request.POST and request.is_ajax():
        updatePetfinderToken()
        response = requests.get(os.getenv('PETFINDER_BASE_URL')+'/v2/animals/'+request.POST['id'], headers={'Authorization': 'Bearer ' + os.getenv('PETFINDER_ACCESS_TOKEN')})
        response = json.loads(response.text)
        if len(response['animal']['photos']):
            default_image = response['animal']['photos'][0]['small']
        else:
            default_image = 'https://placekitten.com/100/150'
        if not Pet.objects.filter(animal_id=response['animal']['id']).exists():
            favorite = Pet(
                animal_id=response['animal']['id'],
                animal_type=response['animal']['type'],
                detail_link=response['animal']['url'],
                image=default_image,
                age=response['animal']['age'],
                gender=response['animal']['gender'],
                size=response['animal']['size'],
                name=response['animal']['name'],
                description=response['animal']['description'],
                status=response['animal']['status'],
                zipcode=response['animal']['contact']['address']['postcode']
            )
            favorite.save()

            return JsonResponse({'message': 'Pet added to favorites'})

        return JsonResponse({'message': 'Pet already exists in favorites'})

def deleteFavorite(request):
    if request.POST and request.is_ajax():
        try:
            favorite = Pet.objects.get(animal_id=request.POST['id'])
            favorite.delete()
        except Exception:
            return JsonResponse({'message': 'Pet is not favorited, no action required'})

    return JsonResponse({'message': 'Pet removed from favorites'})

def listFavorites(request):
    favorites = Pet.objects.all()
    context = {
        'favorites': favorites,
        'google_api_key': os.getenv('GOOGLE_MAPS_API_KEY')
    }
    return render(request, 'petfinder/favorites.html', context)


# helpers
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