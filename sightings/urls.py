from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
        path('sightings/', views.index),
        path('maps/',views.view_map, name='view_map'),
    ]
