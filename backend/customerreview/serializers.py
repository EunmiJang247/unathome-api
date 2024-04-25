from rest_framework import serializers
from .models import Customerreview, CustomerreviewImage

class CustomerreviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customerreview
    fields = '__all__'

class CustomerreviewImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomerreviewImage
    fields = '__all__'