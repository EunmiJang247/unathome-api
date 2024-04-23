from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# id: string
# createdAt: Date
# title(string) / 글 제목
# contents(string) / 글 내용
# address(string/ 시공받은 아파트 이름)
# interiorCompany(string/ 시공업체)
# residentType(주거유형) / 아파트 /오피스텔/ 빌라
# duration(string / 기간)
# likeCount(int/ 좋아요숫자)
# price(int / 가격)
# onAds(bool) => true면은 메인페이지에 보여짐
# size(int / 평형)
# images(array / 대표사진에 보여질 이미지들)
# tags(ForignKey / 테그)

class TypeField(models.TextChoices):
  opistel = '오피스텔'
  apartment = '아파트'
  villa = '빌라'

class Customerreview(models.Model):
  createdAt = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=200, null=True)
  contents = models.TextField(null=True)
  address = models.CharField(max_length=100, null=True)
  interiorCompany = models.CharField(max_length=100, null=True)
  residentType = models.CharField(max_length=20, choices=TypeField,null=True)
  duration = models.CharField(max_length=100, null=True)
  size = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(300)])
  likeCount = models.IntegerField(null=True)
  price = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(1000000000)])
  # images = ArrayField(models.CharField(max_length=200), null=True)
  onAds = models.BooleanField(default=False)
  # tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

  