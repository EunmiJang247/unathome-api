from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from account.serializers import UserSerializer

from .serializers import ConsultantSerializer
from .models import Consultant

from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createConsultant(request):
    data = request.data
    serializer = ConsultantSerializer(data=data)
    
    try:
      if serializer.is_valid():
          print('?')
          serializer.save()
          return Response(serializer.data)
      else:
          raise ValidationError(serializer.errors)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)