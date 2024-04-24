from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from .serializers import InteriorcompanySerializer
from .models import Interiorcompany
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@permission_classes([AllowAny])
def getAllInteriorcompany(request):
  companies = Interiorcompany.objects.all().order_by('id')
  count = companies.count()

  resPerPage = 10
  paginator = PageNumberPagination()
  paginator.page_size = resPerPage

  queryset = paginator.paginate_queryset(companies, request)
  
  serializer = InteriorcompanySerializer(queryset, many=True)
  return Response({
    'count': count,
    'resPerPage': resPerPage,
    'portfolios':serializer.data})