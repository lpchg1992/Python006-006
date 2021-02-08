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
    __tablename__ = 'articles'
    title = models.CharField(max_length=30, verbose_name='文章标题', default='')
    body = models.CharField(max_length=30, verbose_name='文章内容', default='')
    create_time = models.DateTimeField(auto_now_add=True)  # 文章创建时间
    author_id = models.ForeignKey(
        'auth.User', verbose_name='用户id', related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.title



# class ProfileAPI(models.Model):
#     """
#     用户积分
#     """
#     __tablename__ = 'score'
#     score = models.CharField(max_length=10, verbose_name='积分', default='0')
#     owner = models.OneToOneField(
#         'auth.User', related_name="profile_api", on_delete=models.CASCADE)


#     @receiver(post_save, sender=User)
#     def handler_user_create_content(sender, instance, created, **kwargs):
#         if created:
#             ProfileAPI.objects.create(username=instance)

#     @receiver(post_save, sender=User)
#     def handler_user_save_content(sender, instance, created, **kwargs):
#         instance.profile.save()

class Posts(models.Model):
    """
    评论和回复
    """
    __tablename__ = 'posts'
    content = models.CharField(max_length=30, verbose_name='评论内容', default='')
    create_time = models.DateTimeField(auto_now_add=True)  # 评论回复时间
    article_id = models.ForeignKey(
        'Articles', verbose_name='文章id', related_name='art_com', on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        'auth.User', verbose_name='评论用户id', related_name='posts_users', on_delete=models.CASCADE)
    # 如果实现回复需要增加被回复评论id和被回复用户id
    # user_to_id = models.ForeignKey(
    #     'auth.User', verbose_name='被回复用户id' related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title