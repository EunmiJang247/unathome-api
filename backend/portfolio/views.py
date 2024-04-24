from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from .serializers import PortfolioSerializer, PortfolioImageSerializer
from .models import Portfolio, PortfolioImage

from django.shortcuts import get_object_or_404
from .filters import PortfoliosFilter

@api_view(['GET'])
@permission_classes([AllowAny])
def getMainPagePortfolio(request):
    filterset = PortfoliosFilter(request.GET, queryset=Portfolio.objects.filter(onAds=True).order_by('-id')[:6])
    
    portfolios_with_images = []
    for portfolio in filterset.qs:
        portfolio_data = PortfolioSerializer(portfolio).data
        images = PortfolioImage.objects.filter(portfolio=portfolio)
        image_data = PortfolioImageSerializer(images, many=True).data
        portfolio_data['images'] = image_data
        portfolios_with_images.append(portfolio_data)

    return Response(portfolios_with_images)

@api_view(['GET'])
@permission_classes([AllowAny])
def getAllPortfolio(request):
  filterset = PortfoliosFilter(request.GET, queryset=Portfolio.objects.all().order_by('id'))
  count = filterset.qs.count()

  # 페이지네이션을 위해 추가
  resPerPage = 9
  paginator = PageNumberPagination()
  paginator.page_size = resPerPage

  queryset = paginator.paginate_queryset(filterset.qs, request)

  # 포트폴리오와 연관된 이미지 가져오기
  portfolios_with_images = []
  for portfolio in queryset:
      portfolio_data = PortfolioSerializer(portfolio).data

      images = PortfolioImage.objects.filter(portfolio=portfolio)
      image_data = PortfolioImageSerializer(images, many=True).data
      portfolio_data['images'] = image_data
      portfolios_with_images.append(portfolio_data)

  return Response({
    'count': count,
    'resPerPage': resPerPage,
    'portfolios': portfolios_with_images})

@api_view(['GET'])
@permission_classes([AllowAny])
def getPortfolio(request, pk):
  portfolio = get_object_or_404(Portfolio, id=pk)
  portfolio_serializer = PortfolioSerializer(portfolio, many=False)

  # 해당 포트폴리오에 연결된 이미지 가져오기
  images = PortfolioImage.objects.filter(portfolio=portfolio)
  image_serializer = PortfolioImageSerializer(images, many=True)

  # 포트폴리오 정보와 이미지 정보를 합쳐서 응답
  response_data = {
        'portfolio': portfolio_serializer.data,
        'images': image_serializer.data
  }

  return Response(response_data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newPortfolio(request):
  data = request.data

  portfolio_data = {
      'title': data.get('title'),
      'contents': data.get('contents'),
      'address': data.get('address'),
      'interiorCompany': data.get('interiorCompany'),
      'residentType': data.get('residentType'),
      'duration': data.get('duration'),
      'size': data.get('size'),
      'price': data.get('price'),
  }

  # 포트폴리오 정보를 저장
  portfolio = Portfolio.objects.create(**portfolio_data)
  images_data = request.FILES.getlist('images')

  print(images_data)

  # 각 이미지를 포트폴리오에 연결합니다.
  for image_data in images_data:
        PortfolioImage.objects.create(portfolio=portfolio, images=image_data)

  serializer = PortfolioSerializer(portfolio, many=False)
  return Response(serializer.data)

@api_view(['PUT'])
def updatePortfolio(request, pk):
  portfolio = get_object_or_404(Portfolio, id=pk)
  portfolio.title = request.data['title']
  portfolio.contents = request.data['contents']
  portfolio.address = request.data['address']
  portfolio.interiorCompany = request.data['interiorCompany']
  portfolio.residentType = request.data['residentType']
  portfolio.duration = request.data['duration']
  portfolio.size = request.data['size']
  portfolio.price = request.data['price']

  portfolio.save()

  serializer = PortfolioSerializer(portfolio, many=False)
  return Response(serializer.data)

@api_view(['DELETE'])
def deletePortfolio(request, pk):
  portfolio = get_object_or_404(Portfolio, id=pk)
  portfolio.delete()
  return Response({ 'message': 'Job is Delted' }, status=status.HTTP_200_OK)
