from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializer, UserSerializer

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# 카카오로그인
@api_view(['POST'])
def kakaoLogin(request):
  data = request.data
  user = SignUpSerializer(data=data)

  if user.is_valid():
    if not User.objects.filter(username=data['first_name']).exists():
      user = User.objects.create(
        username = data['first_name'],
        password = make_password('unathome')
      )

      # 토큰 발급을 위한 데이터
      token_data = {
          'username': user.username,
          'password': 'unathome'
      }

      # 토큰 발급 엔드포인트 호출
      token_response = TokenObtainPairSerializer().validate(token_data)

      return Response(token_response, status=status.HTTP_200_OK)
    
    else:
      user = User.objects.filter(
        username = data['first_name'],
      ).first()
      token_data = {
        'username': user,
        'password': 'unathome'
      }
      token_response = TokenObtainPairSerializer().validate(token_data)
      return Response(token_response, status=status.HTTP_200_OK)

  else:
    return Response(user.errors)


# 유저 삭제
@api_view(['DELETE'])
def deleteUser(request, pk):
  user = get_object_or_404(User, id=pk)
  user.delete()
  return Response({ 'message': 'User is Delted' }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verifyToken(request):
  user = UserSerializer(request.user)
  return Response(user.data)
