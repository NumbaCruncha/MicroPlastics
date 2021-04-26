# from django.contrib import admin
from django.contrib.gis import admin

from .models import Organisation, FieldUser, Site


class customGeoAdmin(admin.GeoModelAdmin):
    default_lat = -45.87867
    default_lon = 170.49587
    

admin.site.register(Organisation, customGeoAdmin) 
admin.site.register(Site, customGeoAdmin)
admin.site.register(FieldUser, admin.GeoModelAdmin)


