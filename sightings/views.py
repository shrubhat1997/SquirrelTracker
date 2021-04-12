from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrels
from django.shortcuts import redirect, get_object_or_404

from .models import Squirrels
from .forms import SquirrelSightingForm

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

def update(request, squirrel_id):
    object = get_object_or_404(Squirrels, Unique_Squirrel_ID=squirrel_id)
    if request.method=='POST':
        form = SquirrelSightingForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
    else:
        form = SquirrelSightingForm(instance=object)
    context = {
            'form': form,
            }
    return render(request, 'sightings/squirrel_update.html', context)

def add(request):
        if request.method=='POST':
            form = SquirrelSightingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(f'/sightings/')
        else:
            form = SquirrelSightingForm()
        context = {
                    'form': form,
        }
        return render(request, 'sightings/squirrel_add.html', context)

