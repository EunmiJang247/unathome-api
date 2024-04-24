from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from .serializers import StorySerializer, StoryImageSerializer
from .models import Story, StoryImage

from django.shortcuts import get_object_or_404

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