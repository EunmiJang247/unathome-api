from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from account.serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated

from .serializers import StorySerializer
from .models import Story

from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

@api_view(['GET'])
@permission_classes([AllowAny])
def getAllStory(request):
    story = Story.objects.order_by('-id')
    count = story.count()

    resPerPage = 9
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(story, request)
    serializer = StorySerializer(queryset, many=True)

    return Response({
    'count': count,
    'story': serializer.data})


@api_view(['GET'])
def getStory(request, pk):
    story = get_object_or_404(Story, id=pk)

    # 현재 이야기의 id를 기준으로 이전 이야기와 다음 이야기 찾기
    previous_story = Story.objects.filter(id__lt=pk).order_by('-id').first()
    next_story = Story.objects.filter(id__gt=pk).order_by('id').first()

    # 이전 이야기와 다음 이야기가 없을 경우에 대한 처리
    previous_story_data = None
    next_story_data = None
    if previous_story:
        previous_story_data = {
            'id': previous_story.id,
            'title': previous_story.title  # 이전 이야기의 제목 또는 필요한 정보 추가
        }
    if next_story:
        next_story_data = {
            'id': next_story.id,
            'title': next_story.title  # 다음 이야기의 제목 또는 필요한 정보 추가
        }

    user = story.createdBy
    user_serializer = UserSerializer(user)

    serializer = StorySerializer(story, many=False)
    return Response({
        'user': user_serializer.data,
        'story': serializer.data,
        'previous_story': previous_story_data,
        'next_story': next_story_data
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newStoryFunc(request):
    request.data['createdBy'] = request.user

    data = request.data
    customerreview = Story.objects.create(**data)
    serializer = StorySerializer(customerreview, many=False)
    return Response(serializer.data)