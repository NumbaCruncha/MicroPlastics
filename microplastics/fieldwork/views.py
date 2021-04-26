from django.shortcuts import get_object_or_404, render

from .models import Site
from .serializers import SiteSerializer
from rest_framework import generics


# def index(request, site_id):
#     site = get_object_or_404(Site, pk=site_id)
#     return render(request, 'fieldwork/index.html', {'site': site})

def index(request):
    return render(request, 'fieldwork/index.html')

class SiteListCreate(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer