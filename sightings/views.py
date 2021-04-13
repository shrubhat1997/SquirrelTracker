from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrels
from django.shortcuts import redirect, get_object_or_404
from .forms import SquirrelSightingForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

def index(request) :
    squirrels = Squirrels.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(squirrels, 20)
    try:
        squirrels = paginator.page(page)
    except PageNotAnInteger:
        squirrels = paginator.page(1)
    except EmptyPage:
        squirrels = paginator.page(paginator.num_pages)
    
    context = {
        'squirrels' : squirrels,
    }
    return render(request,'sightings/index.html',context)

def map(request) :
    spot = Squirrels.objects.all()
    context = {
            'spot' : spot[:100],
    }
    return render(request,'sightings/map.html',context)

def update(request, squirrel_id):
    object1 = get_object_or_404(Squirrels, Unique_Squirrel_ID=squirrel_id)
    if request.method=='POST':
        form = SquirrelSightingForm(request.POST, instance=object1)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
    else:
        form = SquirrelSightingForm(instance=object1)
    context = {
            'form': form,
            'squirrel_id':squirrel_id,
            }
    return render(request, 'sightings/update.html', context)

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
        return render(request, 'sightings/add.html', context)

def stats(request):

    num_of_sightings = Squirrels.objects.all().count()
    num_of_am_shift = Squirrels.objects.filter(Shift='AM').count()
    num_of_pm_shift = Squirrels.objects.filter(Shift='PM').count()
    num_of_adults = Squirrels.objects.filter(Age='Adult').count()
    num_of_juveniles = Squirrels.objects.filter(Age='Juvenile').count()
    num_groundplane = Squirrels.objects.filter(Location='Ground Plane').count()
    num_aboveground = Squirrels.objects.filter(Location='Above Ground').count()
    
    context = {
        'num_of_am_shift': num_of_am_shift,

        'num_of_pm_shift': num_of_pm_shift,

        'num_of_adults': num_of_adults,

        'num_of_juveniles': num_of_juveniles,

        'num_groundplane':num_groundplane,

        'num_aboveground':num_aboveground,
    }

    return render(request, 'sightings/stats.html', context)
