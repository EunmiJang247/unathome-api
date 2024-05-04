from django.shortcuts import render

from faq import serializers
from .models import Faq
from rest_framework import (
    viewsets,
    mixins,
    status,
)

class BaseRecipeAttrViewSet(mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """Base viewset for recipe attributes."""

# Create your views here.
class FaqViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.FaqSerializer
    queryset = Faq.objects.all()
