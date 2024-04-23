from django.contrib.auth.models import User
from rest_framework import serializers

class SignUpSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')

    extra_kwargs = {
      'first_name': {'required': False, 'allow_blank': False},
      'last_name': {'required': False, 'allow_blank': False},
      'email': {'required': False, 'allow_blank': False},
      'password': {'required': False, 'allow_blank': False},
    }

class UserSerializer(serializers.ModelSerializer):
  bankBook = serializers.FileField(source='userprofile.bankBook')
  address = serializers.CharField(source='userprofile.address')
  class Meta:
    model = User
    fields = ('username', 'bankBook', 'address')