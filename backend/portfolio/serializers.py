from rest_framework import serializers
from .models import Portfolio, PortfolioImage, Tag

class PortfolioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Portfolio
    fields = [
            'id', 'title', 'contents', 'address', 'residentType',
            'duration', 'size', 'likeCount', 'price', 'onAds', 'tags',
        ]

class PortfolioImageSerializer(serializers.ModelSerializer):
  class Meta:
      model = PortfolioImage
      fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
  class Meta:
      model = Tag
      fields = '__all__'