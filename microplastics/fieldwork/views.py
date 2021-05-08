from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.mail import send_mail
from .models import Observation
from .serializers import ObservationSerializer
from rest_framework import generics
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ObservationForm


# def index(request, site_id):
#     site = get_object_or_404(Site, pk=site_id)
#     return render(request, 'fieldwork/index.html', {'site': site})

def observation(request):
    return render(request, 'fieldwork/form.html')

class ObservationListCreate(generics.ListCreateAPIView):
    # queryset = Observation.objects.latest('datetime')
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer


class ObservationCreate(CreateView):
    model = Observation
    form_class = ObservationForm
    success_url = reverse_lazy("thanks")
    
    def thanks(request):
        return HttpResponse("Thank you! Will get in touch soon.")
