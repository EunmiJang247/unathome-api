from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from .serializers import PortfolioSerializer
from .models import Portfolio

from django.shortcuts import get_object_or_404
from .filters import PortfoliosFilter

@api_view(['GET'])
def getMainPagePortfolio(request):
    filterset = PortfoliosFilter(request.GET, queryset=Portfolio.objects.filter(onAds=True).order_by('-id')[:6])
    serializer = PortfolioSerializer(filterset.qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllPortfolio(request):
  filterset = PortfoliosFilter(request.GET, queryset=Portfolio.objects.all().order_by('id'))
  count = filterset.qs.count()

  # 페이지네이션을 위해 추가
  resPerPage = 9
  paginator = PageNumberPagination()
  paginator.page_size = resPerPage

  queryset = paginator.paginate_queryset(filterset.qs, request)
  
  serializer = PortfolioSerializer(queryset, many=True)
  return Response({
    'count': count,
    'resPerPage': resPerPage,
    'portfolios':serializer.data})

@api_view(['GET'])
def getPortfolio(request, pk):
  portfolio = get_object_or_404(Portfolio, id=pk)
  serializer = PortfolioSerializer(portfolio, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def newPortfolio(request):
  data = request.data
  portfolio = Portfolio.objects.create(**data)
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
