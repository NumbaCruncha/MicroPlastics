from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Organisation(models.Model):
    business_name = models.CharField(default=None, max_length=200)
    primary_contact = models.CharField(default=None, max_length=200)    


class FieldUser(models.Model):
    name = models.CharField(default=None, max_length=200)
    contractor = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    

class Site(models.Model):
    code = models.CharField(max_length=5)
    area = models.PolygonField()


class Observation(models.Model):
    id = models.IntegerField(primary_key=True)
    datetime = models.DateTimeField()
    field_user = models.ForeignKey(FieldUser, on_delete=models.CASCADE)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE)