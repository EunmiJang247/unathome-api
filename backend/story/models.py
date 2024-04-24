from django.db import models

# id: string
# title: string
# subTitle: string
# category: string
# contents
# images

class Story(models.Model):
  createdAt = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=200, null=True)
  subTitle = models.CharField(max_length=200, null=True)
  category = models.TextField(null=True)
  contents = models.TextField(null=True)


class StoryImage(models.Model):
    story = models.ForeignKey(Story, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='')