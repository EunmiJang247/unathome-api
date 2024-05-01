from django.db import models
from django.conf import settings

class Consultant(models.Model):
  user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
  )
  woodworking = models.CharField(max_length=50)
  woodworkingCount = models.IntegerField()
  wallpapering = models.CharField(max_length=50)
  wallpaperingCount = models.IntegerField()
  floor = models.CharField(max_length=50)
  floorCount = models.IntegerField()
  bathroom = models.CharField(max_length=50)
  bathroomCount = models.IntegerField()
  sink = models.CharField(max_length=50)
  sinkCount = models.IntegerField()
  demolition = models.CharField(max_length=50)
  demolitionCount = models.IntegerField()
  basic = models.CharField(max_length=50)
  basicCount = models.IntegerField()
  buildingType = models.CharField(max_length=50)
  interiordate=models.DateField()
  address = models.CharField(max_length=150)
  remainaddress = models.CharField(max_length=150)
  customername = models.CharField(max_length=50)
  phonenumber = models.CharField(max_length=50)
  prefertime = models.CharField(max_length=50)
  promotioncode = models.CharField(max_length=50)
  wantstyle = models.CharField(max_length=50)
  personalInfoAgree = models.BooleanField()
  marketingAgree = models.BooleanField()

class ConsultantImage(models.Model):
  consultant = models.ForeignKey(Consultant, related_name='images', on_delete=models.CASCADE)
  images = models.ImageField(upload_to='')