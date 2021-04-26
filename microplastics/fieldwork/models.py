from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

SUBURBS = [
    ('AB', 'Andersons Bay 1'),
    ('EK', 'Ettrick'),
    ('HB', 'Halfway Bush'),
    ('MG', 'Mosegiel 3')
]



class Organisation(models.Model):
    business_name = models.CharField(default=None, max_length=200)
    primary_contact = models.CharField(default=None, max_length=200)    


class FieldUser(models.Model):
    name = models.CharField(default=None, max_length=200)
    contractor = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    

class Site(models.Model):
    code = models.CharField(max_length=5)
    area = models.PolygonField()
    feeder = models.CharField(max_length=200, choices=SUBURBS)
