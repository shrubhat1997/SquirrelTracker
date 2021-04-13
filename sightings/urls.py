from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
        path('sightings/', views.index),
        path('map/',views.map, name='map'),
    ]
