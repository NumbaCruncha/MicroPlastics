from rest_framework import serializers
from .models import Observation

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ('id', 'datetime', 'field_user')


