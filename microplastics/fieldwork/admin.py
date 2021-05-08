# from django.contrib import admin
from django.contrib.gis import admin
from .models import Observation, Organisation, FieldUser


class customGeoAdmin(admin.GeoModelAdmin):
    default_lat = -45.87867
    default_lon = 170.49587
    
admin.site.register(Observation, customGeoAdmin) 
admin.site.register(Organisation, admin.GeoModelAdmin) 
admin.site.register(FieldUser, admin.GeoModelAdmin)


