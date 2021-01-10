from django.db import models


# Create your models here.
class Comments(models.Model):
    # id 自动创建
    stars = models.IntegerField()
    content = models.CharField(max_length=500)
