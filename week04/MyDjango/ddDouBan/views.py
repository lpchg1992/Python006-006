from django.shortcuts import render
from .models import T1
from django.db.models import Avg
# Create your views here.


def books_short(request):
    # 从models取数据传给template
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f"{T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f}"
    # 情感倾向
    sent_avg = f"{T1.objects.aggregate(Avg('sentiment'))['sentiment_avg']:0.2f}"

    # 正向数量
    queryset = T1.objects.values('sentiment')
    conditons = {'sentiment__gte': 0.5}
    plus = queryset.filter(**conditons).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    conditons = {'sentiment__lt': 0.5}
    minus = queryset.filter(**conditons).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())
