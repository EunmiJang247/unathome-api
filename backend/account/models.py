from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  # UserProfile 모델을 사용하면 사용자의 프로필 정보를 User 모델과 별도로 관리할 수 있다.
  user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
  # User가 삭제될 때 해당 UserProfile도 삭제됨을 의미.
  bankBook = models.FileField(null=True)
  address = models.CharField(null=True)
