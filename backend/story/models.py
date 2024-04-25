from django.db import models
from django.contrib.auth.models import User

# id: string
# title: string
# subTitle: string
# category: string
# contents
# images

class Story(models.Model):
  createdAt = models.DateTimeField(auto_now_add=True)
  createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=200, null=True)
  subTitle = models.CharField(max_length=200, null=True)
  category = models.TextField(null=True)
  contents = models.TextField(null=True)
