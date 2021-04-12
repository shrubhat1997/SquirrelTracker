from django.urls import path
from . import views
from django.conf.urls import url

apps_name = 'sightings'

urlpatterns = [
        path('', views.index),
        path('map/',views.view_map, name='view_map'),
        path('<str:Unique_Squirrel_ID>/', views.update, name='update'),
        path('add/', views.add, name='add'),
    ]
