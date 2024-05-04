from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from account.serializers import UserSerializer
from interiorcompany.serializers import InteriorcompanySerializer
from interiorcompany.models import Interiorcompany

from .serializers import PortfolioLikeSerializer, PortfolioSerializer, PortfolioImageSerializer, TagSerializer
from .models import Portfolio, PortfolioImage, PortfolioLike, Tag

from django.shortcuts import get_object_or_404
from .filters import PortfoliosFilter
from portfolio import serializers

from rest_framework import (
    viewsets,
    mixins,
    status,
)

# 포트폴리오 메인 6개
@api_view(['GET'])
@permission_classes([AllowAny])
def getMainPagePortfolio(request):
    size_range = request.GET.get('size_range')  # size 범위를 받아옴
    price_range = request.GET.get('price_range')  # price 범위를 받아옴

    # size_range 파싱
    if size_range:
        size_min, size_max = map(int, size_range.split('-'))
    else:
        size_min, size_max = 10, 200  # 기본값 설정

    # price_range 파싱
    if price_range:
        price_min, price_max = map(int, price_range.split('-'))
    else:
        price_min, price_max = 0, 1000000000  # 기본값 설정

    # 포트폴리오 필터링
    filterset = PortfoliosFilter(request.GET, queryset=Portfolio.objects.filter(
        onAds=True, size__range=(size_min, size_max), price__range=(price_min, price_max)).order_by('-id')[:6])
      
    portfolios_with_images = []
    for portfolio in filterset.qs:
        portfolio_data = PortfolioSerializer(portfolio).data

        tags = portfolio.tags.all()
        tag_data = TagSerializer(tags, many=True).data

        portfolio_data['tags'] = tag_data

        images = PortfolioImage.objects.filter(portfolio=portfolio)
        image_data = PortfolioImageSerializer(images, many=True).data

        portfolio_data['images'] = image_data
        portfolios_with_images.append(portfolio_data)

    return Response(portfolios_with_images)


# 포트폴리오 메인 4개
@api_view(['GET'])
@permission_classes([AllowAny])
def getMainPageKeywordsPortfolio(request):
    keyword = request.GET.get('keyword')  # size 범위를 받아옴
    print(keyword)

    # 포트폴리오 필터링
    filterset = PortfoliosFilter(request.GET, queryset=Portfolio.objects.filter(
        tags__name__icontains=keyword).order_by('-id')[:4])
      
    portfolios_with_images = []
    for portfolio in filterset.qs:
        portfolio_data = PortfolioSerializer(portfolio).data

        tags = portfolio.tags.all()
        tag_data = TagSerializer(tags, many=True).data

        portfolio_data['tags'] = tag_data

        images = PortfolioImage.objects.filter(portfolio=portfolio)
        image_data = PortfolioImageSerializer(images, many=True).data

        portfolio_data['images'] = image_data
        portfolios_with_images.append(portfolio_data)

    return Response(portfolios_with_images)


@api_view(['GET'])
@permission_classes([AllowAny])
def getAllPortfolio(request):
  filterset = PortfoliosFilter(request.GET, queryset=Portfolio.objects.all().order_by('-id'))
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

      tags = portfolio.tags.all()
      tag_data = TagSerializer(tags, many=True).data

      portfolio_data['tags'] = tag_data

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

  # 포트폴리오에 연결된 interiorCompany 정보 가져오기
  interior_company_serializer = None
  if portfolio.interiorCompany:
      interior_company_serializer = InteriorcompanySerializer(portfolio.interiorCompany, many=False)

  return Response({
    'portfolio': portfolio_serializer.data,
    'images': image_serializer.data,
    'interior_company': interior_company_serializer.data if interior_company_serializer else None
  })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newPortfolio(request):
  data = request.data

  # 태그 정보를 추출
  tag_names = data.get('tags', [])
  tags = []
  for tag_name in tag_names:
      tag, _ = Tag.objects.get_or_create(name=tag_name)
      tags.append(tag.pk)

  interior_company_id = data.get('interiorCompany')

  try:
    interior_company = Interiorcompany.objects.get(pk=interior_company_id)

  except Interiorcompany.DoesNotExist:
    return Response({"error": "Specified interior company does not exist."}, status=status.HTTP_400_BAD_REQUEST)

  portfolio_data = {
      'title': data.get('title'),
      'contents': data.get('contents'),
      'address': data.get('address'),
      'interiorCompany': interior_company,
      'residentType': data.get('residentType'),
      'duration': data.get('duration'),
      'size': int(data.get('size')),
      'price': int(data.get('price')),
      'tags': tags,
  }
  
  serializer = PortfolioSerializer(data=portfolio_data)
  if serializer.is_valid():
      portfolio = serializer.save()

      # 포트폴리오 이미지 처리
      images_data = request.FILES.getlist('images')
      for image_data in images_data:
          PortfolioImage.objects.create(portfolio=portfolio, images=image_data)

      return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updatePortfolio(request, pk):
  portfolio = get_object_or_404(Portfolio, id=pk)

  if serializer.is_valid():
     portfolio = serializer.save()

     portfolio.title = request.data['title']
     portfolio.contents = request.data['contents']
     portfolio.address = request.data['address']
     portfolio.interiorCompany = request.data['interiorCompany']
     portfolio.residentType = request.data['residentType']
     portfolio.duration = request.data['duration']
     portfolio.size = request.data['size']
     portfolio.price = request.data['price']
     portfolio.tags = request.data['tags']

  portfolio.save()

  serializer = PortfolioSerializer(portfolio, many=False)
  return Response(serializer.data)

@api_view(['DELETE'])
def deletePortfolio(request, pk):
  portfolio = get_object_or_404(Portfolio, id=pk)
  portfolio.delete()
  return Response({ 'message': 'Job is Delted' }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likePortfolio(request, pk):
    portfolio = get_object_or_404(Portfolio, id=pk)
    user = UserSerializer(request.user)
    like_data = {
        'user': user.data['id'],
        'portfolio': portfolio.id,
    }
    serializer = PortfolioLikeSerializer(data=like_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myLikePortfolios(request):
    user = UserSerializer(request.user)
    userId = user.data['id']

    filterset = PortfolioLike.objects.filter(user_id=userId).order_by('-id')
    count = filterset.count()

    resPerPage = 9
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset, request)

    portfolios_with_images = []
    for portfolio_like in queryset:
        portfolio = portfolio_like.portfolio
        portfolio_data = PortfolioSerializer(portfolio).data

        images = PortfolioImage.objects.filter(portfolio=portfolio)
        image_data = PortfolioImageSerializer(images, many=True).data
        
        portfolio_data['images'] = image_data
        portfolios_with_images.append(portfolio_data)

    return Response({
        'count': count,
        'resPerPage': resPerPage,
        'portfolios': portfolios_with_images})


# 사용자가 좋아요한 게시물 목록을 가져옵니다.
# def get_liked_posts(user):
#     liked_posts = PortfolioLike.objects.filter(user=user).values_list('post_id', flat=True)
#     return liked_posts


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def isPostLiked(request, pk):
# 해당 게시물이 사용자가 좋아요한 게시물인지 여부를 확인합니다.
    user = UserSerializer(request.user)
    userId = user.data['id']
    # return post_id in liked_posts

class BaseRecipeAttrViewSet(mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """Base viewset for recipe attributes."""

class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()

class PortpolioLikeViewSet(BaseRecipeAttrViewSet):
    """PortpolioLikeViewSet database."""
    serializer_class = serializers.PortfolioLikeSerializer
    queryset = PortfolioLike.objects.all()
