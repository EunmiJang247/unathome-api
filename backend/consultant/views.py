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
from interiorcompany.models import Interiorcompany
from interiorcompany.serializers import InteriorcompanySerializer

from .serializers import ConsultantSerializer, ConsultantImageSerializer
from .models import Consultant, ConsultantImage
from rest_framework.exceptions import PermissionDenied

from django.shortcuts import get_object_or_404

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyConsultant(request):
  user = UserSerializer(request.user)
  userId = user.data['id']

  filterset = Consultant.objects.filter(createdBy_id=userId).order_by('-id')
  count = filterset.count()

  # 페이지네이션을 위해 추가
  resPerPage = 10
  paginator = PageNumberPagination()
  paginator.page_size = resPerPage

  queryset = paginator.paginate_queryset(filterset, request)

  # 리뷰와 이미지 모두
  consultant_with_images = []
  for consultant in queryset:
    consultant_data = ConsultantSerializer(consultant).data

    images = ConsultantImage.objects.filter(consultant=consultant)
    image_data = ConsultantImageSerializer(images, many=True).data

    consultant_data['images'] = image_data
    consultant_with_images.append(consultant_data)
  
  return Response({
    'count': count,
    'resPerPage': resPerPage,
    'customerReview': consultant_with_images})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createConsultant(request):
    data = request.data.copy()
    data['createdBy'] = request.user.id


    serializer = ConsultantSerializer(data=data)
    
    try:
      if serializer.is_valid():
          consultant = serializer.save()
          images_data = request.FILES.getlist('images')

          for image_data in images_data:
            ConsultantImage.objects.create(consultant=consultant, images=image_data)

          return Response(serializer.data)
      else:
          raise ValidationError(serializer.errors)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def readConsultant(request, pk):
  user = UserSerializer(request.user)
  consultant = get_object_or_404(Consultant, id=pk)
  consultant_serializer = ConsultantSerializer(consultant, many=False)
  userId = user.data['id']

  if userId != consultant.createdBy.id:
    raise PermissionDenied("You don't have permission to access this consultant.")

  interiorCompany = InteriorcompanySerializer(consultant.interiorCompany, many=False)
  images = ConsultantImage.objects.filter(consultant=consultant)
  image_serializer = ConsultantImageSerializer(images, many=True)

  return Response({
    'consultant': consultant_serializer.data,
    'images': image_serializer.data,
    'interiorCompany': interiorCompany.data,
  })