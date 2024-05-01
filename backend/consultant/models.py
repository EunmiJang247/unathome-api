from django.db import models
from django.contrib.auth.models import User

class Consultant(models.Model):
  createdAt = models.DateTimeField(auto_now_add=True)
  createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  woodworking = models.CharField(max_length=50, null=True)
  woodworkingCount = models.IntegerField(null=True)
  wallpapering = models.CharField(max_length=50, null=True)
  wallpaperingCount = models.IntegerField(null=True)
  floor = models.CharField(max_length=50, null=True)
  floorCount = models.IntegerField(null=True)
  bathroom = models.CharField(max_length=50, null=True)
  bathroomCount = models.IntegerField(null=True)
  sink = models.CharField(max_length=50, null=True)
  sinkCount = models.IntegerField(null=True)
  demolition = models.CharField(max_length=50, null=True)
  demolitionCount = models.IntegerField(null=True)
  basic = models.CharField(max_length=50, null=True)
  basicCount = models.IntegerField(null=True)
  buildingType = models.CharField(max_length=50, null=True)
  interiordate=models.DateField(null=True)
  address = models.CharField(max_length=150, null=True)
  remainaddress = models.CharField(max_length=150, null=True)
  customername = models.CharField(max_length=50, null=True)
  phonenumber = models.CharField(max_length=50, null=True)
  prefertime = models.CharField(max_length=50, null=True)
  promotioncode = models.CharField(max_length=50, null=True)
  wantstyle = models.CharField(max_length=50, null=True)
  personalInfoAgree = models.BooleanField(default=False)
  marketingAgree = models.BooleanField(default=False)

class ConsultantImage(models.Model):
  consultant = models.ForeignKey(Consultant, related_name='images', on_delete=models.CASCADE)
  images = models.ImageField(upload_to='', null=True)