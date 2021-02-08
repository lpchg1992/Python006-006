from django.db import models

# Create your models here.
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings



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

# https://docs.djangoproject.com/zh-hans/2.2/topics/auth/customizing/#extending-django-s-default-user

class UserProfile(models.Model):
    username = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, verbose_name='昵称', default='')
    phone_number = models.CharField(max_length=20, verbose_name='手机', unique=True, blank=True)
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    description = models.CharField(max_length=30, verbose_name='个人简介', default='')
    score = models.BigIntegerField(verbose_name='积分', default=0)

    # objects = UserManager()

    @classmethod
    def get_blacklist(cls):
        # seek that is_active = False
        return cls.objects.filter(is_active=False)

    class Meta:
        verbose_name = 'User Profile'
        # proxy = True
 

    # 当生成 user 的时候自动生成 UserProfile
    # 原型是: receiver(signal, **kwargs), 当User产生post_save信号时 
    @receiver(post_save, sender=User)  
    def handler_user_create_content(sender, instance, created, **kwargs):
        # 如果第一次创建
        if created:  
            # 绑定User实例到UserProfile的username字段
            UserProfile.objects.create(username=instance)  
        
    @receiver(post_save, sender=User)  
    def handler_user_save_content(sender, instance, created, **kwargs):
        # profile = UserProfile.objects.create(username=instance)
        # 保存UserProfile的内容 ,profile是username字段外键的related_name名
        instance.profile.save()  

