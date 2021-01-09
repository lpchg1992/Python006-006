from django.shortcuts import render
from .models import T1
from django.db.models import Avg
# Create your views here.


def books_short(request):
    # 从models取数据传给template【queryset数据类型可以用python方法处理】
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    # 聚合函数返回字典
    star_avg = f"{T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f}"
    # 情感倾向
    sent_avg = f"{T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"

    # 正向数量
    queryset = T1.objects.values('sentiment')
    # 双下划线前面：字段，后面：判断条件：
    # 判断条件通常有：gte:>=   gt:>  lt:<  lte:<=
    conditons = {'sentiment__gte': 0.5}
    # 过滤
    plus = queryset.filter(**conditons).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    conditons = {'sentiment__lt': 0.5}
    minus = queryset.filter(**conditons).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())
