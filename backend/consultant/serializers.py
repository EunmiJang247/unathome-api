from rest_framework import serializers
from .models import Consultant, ConsultantImage

class ConsultantSerializer(serializers.ModelSerializer):
  class Meta:
    model = Consultant
    fields = '__all__'
    extra_kwargs = {
      'wallpapering': {'required': False},
      'floor': {'required': False},
      'bathroom': {'required': False},
      'sink': {'required': False},
      'demolition': {'required': False},
      'basic': {'required': False},
    }
    
class ConsultantImageSerializer(serializers.ModelSerializer):
  class Meta:
      model = ConsultantImage
      fields = '__all__'