from django.db import models


# Create your models here.
# 图书 or 电影
class Type(models.Model):
    # id = models.AutoField(primary_key=True) # Django自动创建并设置为主键
    typename = models.CharField(max_length=20)


# 作品名称作者主演
class Name(models.Model):
    # id 自动创建
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=5)
