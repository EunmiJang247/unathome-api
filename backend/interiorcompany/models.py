from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# id: string
# createdAt: Date
# name: string
# contactNumber: string
# location: string
# email: string(optional)
# image
# averageRating

class Interiorcompany(models.Model):
  createdAt = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100, null=True)
  contactNumber = models.CharField(max_length=100, null=True)
  location = models.CharField(max_length=100, null=True)
  email = models.CharField(max_length=100, null=True)
  image = models.FileField(null=True)
  averageRating = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
