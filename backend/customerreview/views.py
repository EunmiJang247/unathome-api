from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from .serializers import CustomerreviewSerializer
from .models import Customerreview

from django.shortcuts import get_object_or_404
from .filters import CustomerreviewFilter


@api_view(['GET'])
def getAllCustomerReview(request):
  filterset = CustomerreviewFilter(request.GET, queryset=Customerreview.objects.all().order_by('id'))
  count = filterset.qs.count()

  # 페이지네이션을 위해 추가
  resPerPage = 9
  paginator = PageNumberPagination()
  paginator.page_size = resPerPage

  queryset = paginator.paginate_queryset(filterset.qs, request)
  
  serializer = CustomerreviewSerializer(queryset, many=True)
  return Response({
    'count': count,
    'resPerPage': resPerPage,
    'customerReview':serializer.data})


@api_view(['GET'])
def getMainPageCustomerReview(request):
    filterset = CustomerreviewFilter(request.GET, queryset=Customerreview.objects.filter(onAds=True).order_by('-id')[:6])
    serializer = CustomerreviewSerializer(filterset.qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCustomerReview(request, pk):
  customerreview = get_object_or_404(Customerreview, id=pk)
  serializer = CustomerreviewSerializer(customerreview, many=False)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newCustomerReview(request):
  request.data['createdBy'] = request.user

  data = request.data
  customerreview = Customerreview.objects.create(**data)
  serializer = CustomerreviewSerializer(customerreview, many=False)
  return Response(serializer.data)

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
def deleteCustomerReview(request, pk):
  portfolio = get_object_or_404(Customerreview, id=pk)
  portfolio.delete()
  return Response({ 'message': 'Customer Review is Deleted' }, status=status.HTTP_200_OK)
