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
        form = SquirrelSightingForm(instance=object)
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
