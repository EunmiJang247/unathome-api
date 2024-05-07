from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from account.serializers import UserSerializer
from interiorcompany.serializers import InteriorcompanySerializer

from .serializers import CustomerreviewSerializer, CustomerreviewImageSerializer
from .models import Customerreview, CustomerreviewImage

from django.shortcuts import get_object_or_404
from .filters import CustomerreviewFilter


@api_view(['GET'])
@permission_classes([AllowAny])
def getMainPageCustomerReview(request):
    filterset = CustomerreviewFilter(request.GET, queryset=Customerreview.objects.filter(onAds=True).order_by('-id')[:6])
    
    customer_review_with_images = []
    for customerriew in filterset.qs:
        customerriew_data = CustomerreviewSerializer(customerriew).data
        images = CustomerreviewImage.objects.filter(review=customerriew)
        image_data = CustomerreviewImageSerializer(images, many=True).data
        customerriew_data['images'] = image_data
        customer_review_with_images.append(customerriew_data)

    serializer = CustomerreviewSerializer(filterset.qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def getAllCustomerReview(request):
  filterset = CustomerreviewFilter(request.GET, queryset=Customerreview.objects.all().order_by('-id'))
  count = filterset.qs.count()

  # 페이지네이션을 위해 추가
  resPerPage = 9
  paginator = PageNumberPagination()
  paginator.page_size = resPerPage

  queryset = paginator.paginate_queryset(filterset.qs, request)

  # 리뷰와 이미지 모두
  review_with_images = []
  for review in queryset:
    review_data = CustomerreviewSerializer(review).data

    images = CustomerreviewImage.objects.filter(review=review)
    image_serializer = CustomerreviewImageSerializer(images, many=True)

    image_data = image_serializer.data
    review_data['images'] = image_data
    review_with_images.append(review_data)
  
  return Response({
    'count': count,
    'resPerPage': resPerPage,
    'customerReview': review_with_images})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyCustomerReview(request):
  user = UserSerializer(request.user)
  userId = user.data['id']

  filterset = CustomerreviewFilter(request.GET, queryset=Customerreview.objects.filter(createdBy=userId).order_by('-id'))
  count = filterset.qs.count()

  # 페이지네이션을 위해 추가
  resPerPage = 9
  paginator = PageNumberPagination()
  paginator.page_size = resPerPage

  queryset = paginator.paginate_queryset(filterset.qs, request)

  # 리뷰와 이미지 모두
  review_with_images = []
  for review in queryset:
    review_data = CustomerreviewSerializer(review).data

    images = CustomerreviewImage.objects.filter(review=review)
    image_serializer = CustomerreviewImageSerializer(images, many=True)

    image_data = image_serializer.data
    review_data['images'] = image_data
    review_with_images.append(review_data)
  
  return Response({
    'count': count,
    'resPerPage': resPerPage,
    'customerReview': review_with_images})


@api_view(['GET'])
@permission_classes([AllowAny])
def getCustomerReview(request, pk):
  customerreview = get_object_or_404(Customerreview, id=pk)

  # 현재 리뷰의 id를 기준으로 이전글과 다음글 찾기
  previous_review = Customerreview.objects.filter(id__lt=pk).order_by('-id').first()
  next_review = Customerreview.objects.filter(id__gt=pk).order_by('id').first()

  # 이전글과 다음글이 없을 경우에 대한 처리
  previous_review_data = None
  next_review_data = None
  if previous_review:
      previous_review_data = {
          'id': previous_review.id,
          'title': previous_review.title  # 이전글의 제목 또는 필요한 정보 추가
      }
  if next_review:
      next_review_data = {
          'id': next_review.id,
          'title': next_review.title  # 다음글의 제목 또는 필요한 정보 추가
      }

  # 리뷰에 대한 유저 정보 가져오기
  user = customerreview.createdBy


  # 유저 정보 시리얼라이즈
  user_serializer = UserSerializer(user)
  review_serializer = CustomerreviewSerializer(customerreview, many=False)

  # 해당 리뷰에 연결된 이미지 가져오기
  images = CustomerreviewImage.objects.filter(review=customerreview)
  image_serializer = CustomerreviewImageSerializer(images, many=True)

  # 업체정보 가져오기
  interior_company = InteriorcompanySerializer(customerreview.interiorCompany, many=False)

  return Response({
      'user': user_serializer.data,
      'review': review_serializer.data,
      'previous_review': previous_review_data,
      'next_review': next_review_data,
      'images': image_serializer.data,
      'interiorCompany': interior_company.data,
  })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newCustomerReview(request):
  data = request.data
  review_data = {
    'address': data.get('address'),
    'contents': data.get('contents'),
    'duration': data.get('duration'),
    'interiorCompany': data.get('interiorCompany'),
    'intimacyRating': data.get('intimacyRating'),
    'price': data.get('price'),
    'priceRating': data.get('priceRating'),
    'qualityRating': data.get('qualityRating'),
    'residentType': data.get('residentType'),
    'title': data.get('title'),
    'totalRating': data.get('totalRating'),
    'createdBy': request.user.id,
    'size': data.get('size'),
  }

  serializer = CustomerreviewSerializer(data=review_data)
  if serializer.is_valid():
      review = serializer.save()

      # 포트폴리오 이미지 처리
      images_data = request.FILES.getlist('images')
      for image_data in images_data:
          CustomerreviewImage.objects.create(review=review, images=image_data)

      return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCustomerReview(request, pk):
  customerreview = get_object_or_404(Customerreview, id=pk)

  if customerreview.createdBy != request.user:
    return Response({'message': 'You can not update this job'}, status=status.HTTP_403_FORBIDDEN)

  customerreview.title = request.data['title']
  customerreview.contents = request.data['contents']
  customerreview.address = request.data['address']
  customerreview.interiorCompany = request.data['interiorCompany']
  customerreview.residentType = request.data['residentType']
  customerreview.duration = request.data['duration']
  customerreview.size = request.data['size']
  customerreview.price = request.data['price']

  customerreview.save()

  serializer = CustomerreviewSerializer(customerreview, many=False)
  return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCustomerReview(request, pk):
  customerreview = get_object_or_404(Customerreview, id=pk)
  print(customerreview)

  # if customerreview.createdBy != request.user:
  #   return Response({'message': 'You can not update this job'}, status=status.HTTP_403_FORBIDDEN)

  customerreview.delete()
  return Response({ 'message': 'Customer Review is Deleted' }, status=status.HTTP_200_OK)
