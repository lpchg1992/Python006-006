from django.db import models

# Create your models here.


class Orders(models.Model):
    """
    订单
    """
    _tablename_ = 'orders'
    title = models.CharField(max_length=30, verbose_name='订单标题')
    details = models.CharField(max_length=100, verbose_name='订单详情')

    def __str__(self):
        return self.title
