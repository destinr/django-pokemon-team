from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
import random
import pprint
import json

def index(request):
    return render(request, "index.html")

def teamPage(request):
    endpoint = 'https://pokeapi.co/api/v2/pokemon/'
    pokeID = random.randint(1, 1154)
    
    response = requests.get(endpoint+str(pokeID))
    responseJSON = json.loads(response.text)
    
    pp = pprint.PrettyPrinter(indent=2,depth=2)
    pp.pprint(responseJSON)
    
    origTypeURL = responseJSON['types'][1]['type']['url']
    origPic = responseJSON['sprites']['other']['official-artwork']['front_default']
    print(origTypeURL)
    
    typePokemon = requests.get(origTypeURL)
    typePokeJSON = json.loads(typePokemon.text)
    pokePics = []
    for i in range(5):
        pokeURL = typePokeJSON['pokemon'][i]['pokemon']['url']
        pokeResponse = requests.get(pokeURL)
        pokeResponseJSON = json.loads(pokeResponse.text)
        pokePic = pokeResponseJSON['sprites']['other']['official-artwork']['front_default']
        pokePics.append(pokePic)
    
    myData = {
        'origPic': origPic,
        'addlPics': pokePics
    }
    print(myData)
    
    return render(request,"teamPage.html", myData)

    
    
    
