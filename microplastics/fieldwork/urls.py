from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'fieldwork'

urlpatterns = [
    # path('', views.index, name='index'),
    path('api/fieldwork/', views.ObservationListCreate.as_view()),
    path('observation/', views.observation, name="observation")
    ]