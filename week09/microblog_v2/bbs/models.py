from django.db import models

# Create your models here.
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.conf import settings
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# User = get_user_model()


class Articles(models.Model):
    """
    文章
    """
    articleid = models.CharField(
        max_length=30, verbose_name='文章id', default='')
    title = models.CharField(max_length=30, verbose_name='文章标题', default='')
    
    article = models.CharField(max_length=30, verbose_name='文章内容', default='')
    createtime = models.DateTimeField(auto_now_add=True)

    # 第一次migrations需注释掉owner
    # owner = models.CharField(max_length=30, default='first migrate')
    owner = models.ForeignKey(
        'auth.User', related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ['createtime']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        super(Articles, self).save(*args, **kwargs)


