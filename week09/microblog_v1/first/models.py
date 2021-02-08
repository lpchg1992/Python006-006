from django.db import models

# Create your models here.
from datetime import datetime


class Articles(models.Model):
    """
    文章
    """
    articleid = models.CharField(
        max_length=30, verbose_name='文章id', default='')
    article = models.CharField(max_length=30, verbose_name='文章内容', default='')
    createtime = models.DateTimeField(auto_now_add=True)
    # 第一次migrations需注释掉owner,因为此时auth.User还没有创建。
    owner = models.ForeignKey(
        'auth.User', related_name='articles', on_delete=models.CASCADE)

    # 设置按照创建时间进行序列化操作
    class Meta:
        ordering = ['createtime']

    # 说明功能
    def __str__(self):
        return self.title

    # 模型保存时，如果需要增加操作，可以在这个模块进行操作。
    def save(self, *args, **kwargs):

        super(Articles, self).save(*args, **kwargs)