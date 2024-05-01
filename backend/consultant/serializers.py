from rest_framework import serializers
from .models import Consultant, ConsultantImage

class ConsultantSerializer(serializers.ModelSerializer):
  class Meta:
    model = Consultant
    fields = '__all__'
    
class ConsultantImageSerializer(serializers.ModelSerializer):
  class Meta:
      model = ConsultantImage
      fields = '__all__'