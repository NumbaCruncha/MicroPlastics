from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from django.urls import reverse_lazy


def index(request):
    return render(request, 'frontend/index.html')




