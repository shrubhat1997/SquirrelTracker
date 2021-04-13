from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
        path('sightings/', views.index),
        path('map/',views.map, name='map'),
        path('sightings/add/', views.add, name='add'),
        path('sightings/<squirrel_id>/', views.update, name='update'),
    ]
