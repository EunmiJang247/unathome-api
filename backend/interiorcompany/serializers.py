from rest_framework import serializers
from .models import Interiorcompany

class InteriorcompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Interiorcompany
    fields = '__all__'