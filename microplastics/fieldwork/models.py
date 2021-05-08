from django.contrib.gis.db import models
from django.contrib.gis.db.models.fields import PointField
from django.contrib.gis.geos import Point, Polygon
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

DEFAULT_LOCATION = (-45.87867, 170.49587)

class Organisation(models.Model):
    org_name = models.CharField(default=None, max_length=200)
    pri_contact_fname = models.CharField(default=None, max_length=200)    
    pri_contact_lname = models.CharField(default=None, max_length=200)


class FieldUser(models.Model):
    fname = models.CharField(default=None, max_length=200)
    lname = models.CharField(default=None, max_length=200)

    
class Observation(models.Model):
    datetime = models.DateTimeField()
    sample_type = models.CharField(default=None, max_length=200)
    field_user = models.ForeignKey(FieldUser, on_delete=models.CASCADE)
    location = PointField(default=Point(DEFAULT_LOCATION))

    def str(self):
        return self.datetime

    def __repr__(self):
        return str(self.datetime)

    # def clean(self):
    #     if self.sample_type == '' and self.datetime is not None:
    #         raise ValidationError(
    #             {
    #             'datetime': _('Record does not have a sample')
    #             }
    #             )


