from rest_framework import serializers
from .models import Customerreview

class CustomerreviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customerreview
    fields = '__all__'