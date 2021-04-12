from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
        path('sightings/', views.index),
        path('sightings/maps/',views.view_map, name='view_map'),
        path('sightings/<squirrel_id>/', views.update, name='update'),
        path('sighthings/add/', views.add, name='add'),
    ]
