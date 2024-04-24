from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from .validators import validate_file_extension


from .serializers import InteriorcompanySerializer
from .models import Interiorcompany
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newInteriorcompany(request):
    data = request.data
    serializer = InteriorcompanySerializer(data=data)

    companyImage = request.FILES['image']
    file_path = companyImage.name
    isValidFile = validate_file_extension(file_path)

    if not isValidFile:
        return Response({'error': '파일형식이 잘못되었습니다'})
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        raise ValidationError(serializer.errors)
    