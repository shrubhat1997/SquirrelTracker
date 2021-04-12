from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrels
from django.shortcuts import redirect, get_object_or_404
def index(request) :
    squirrels = Squirrels.objects.all()
    context = {
        'squirrels' : squirrels,
    }
    return render(request,'sightings/index.html',context)
def view_map(request) :
    spot = Squirrels.objects.all()
    context = {
        'spot' : spot,
    }
    return render(request,'sightings/maps.html',context)
