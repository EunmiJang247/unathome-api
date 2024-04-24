from rest_framework import serializers
from .models import Portfolio, PortfolioImage

class PortfolioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Portfolio
    fields = '__all__'

class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = '__all__'