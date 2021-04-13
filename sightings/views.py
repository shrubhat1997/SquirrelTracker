from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrels
from django.shortcuts import redirect, get_object_or_404
from .forms import SquirrelSightingForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    num_of_squirrels = Squirrel.objects.filter(Unique_Squirrel_ID).count()
    num_of_am_shift = Squirrels.objects.filter(Shift='AM').count()
    num_of_pm_shift = Squirrels.objects.filter(Shift='PM').count()
    num_of_adults = Squirrels.objects.filter(Age='Adult').count()
    num_of_juveniles = Squirrels.objects.filter(Age='Juvenile').count()
    num_of_gray = Squirrels.objects.filter(Primary_Fur_Color='Gray').count()
    num_of_cinnamon = Squirrels.objects.filter(Primary_Fur_Color='Cinnamon').count()
    num_of_black = Squirrels.objects.filter(Primary_Fur_Color='Black').count()
    num_of_running = Squirrels.objects.filter(Running).count()
    num_of_chasing = Squirrels.objects.filter(Chasing).count()
    num_of_climbing = Squirrels.objects.filter(Climbing).count()
    num_of_eating = Squirrels.objects.filter(Eating).count()
    num_of_foraging = Squirrels.objects.filter(Foraging).count()
    num_of_other_activities = Squirrels.objects.filter(Other_Activities).count()
    
    context = {
        'num_of_sightings': num_of_sightings,

        'num_of_squirrels': num_of_squirrels,

        'num_of_am_shift': num_of_am_shift,

        'num_of_pm_shift': num_of_pm_shift,

        'num_of_adults': num_of_adults,

        'num_of_juveniles': num_of_juveniles,

        'num_of_gray': num_of_gray,

        'num_of_cinnamon': num_of_cinnamon,
        'num_of_black': num_of_black,
        'num_of_running': num_of_running,
        'num_of_eating': num_of_eating,
        'num_of_foraging': num_of_foraging,
        'num_of_other_activities': num_of_other_activities,
    }

    return render(request, 'sightings/stats.html', context)
