from django.db import models

class Faq(models.Model):
  createdAt = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=200, null=True)
  contents = models.TextField(null=True)