from rest_framework import serializers
from .models import Story, StoryImage

class StorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Story
    fields = '__all__'

class StoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryImage
        fields = '__all__'