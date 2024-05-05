from django.db import models
from django.contrib.auth.models import User

class TypeField(models.TextChoices):
  접수 = '접수'
  진행중 = '진행중'
  상담완료 = '상담완료'
  공사진행중 = '공사진행중'
  공사완료 = '공사완료'
  후기작성완료 = '후기작성완료'

class Consultant(models.Model):
  createdAt = models.DateTimeField(auto_now_add=True)
  createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  woodworking = models.CharField(max_length=50, null=True, blank=True)
  woodworkingCount = models.IntegerField(null=True, blank=True)
  wallpapering = models.CharField(max_length=50, null=True, blank=True)
  wallpaperingCount = models.IntegerField(null=True, blank=True)
  floor = models.CharField(max_length=50, null=True, blank=True)
  floorCount = models.IntegerField(null=True, blank=True)
  bathroom = models.CharField(max_length=50, null=True, blank=True)
  bathroomCount = models.IntegerField(null=True, blank=True)
  sink = models.CharField(max_length=50, null=True, blank=True)
  sinkCount = models.IntegerField(null=True, blank=True)
  demolition = models.CharField(max_length=50, null=True, blank=True)
  demolitionCount = models.IntegerField(null=True, blank=True)
  basic = models.CharField(max_length=50, null=True, blank=True)
  basicCount = models.IntegerField(null=True, blank=True)
  buildingType = models.CharField(max_length=50, null=True, blank=True)
  interiordate=models.DateField(null=True, blank=True)
  address = models.CharField(max_length=150, null=True, blank=True)
  remainaddress = models.CharField(max_length=150, null=True, blank=True)
  customername = models.CharField(max_length=50, null=True, blank=True)
  phonenumber = models.CharField(max_length=50, null=True, blank=True)
  prefertime = models.CharField(max_length=50, null=True, blank=True)
  promotioncode = models.CharField(max_length=50, null=True, blank=True)
  wantstyle = models.CharField(max_length=50, null=True, blank=True)
  personalInfoAgree = models.BooleanField(default=False)
  marketingAgree = models.BooleanField(default=False)
  status = models.CharField(max_length=20, choices=TypeField,null=True)

class ConsultantImage(models.Model):
  consultant = models.ForeignKey(Consultant, related_name='images', on_delete=models.CASCADE)
  images = models.ImageField(upload_to='', null=True)