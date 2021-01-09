from django.urls import path, re_path, register_converter
from . import views, converters


# 自定义规则
# 规则类在converters文件中
register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')


# 从上往下加载，成功匹配一次结束
urlpatterns = [
    path('', views.index),


    #  带变量的URL
    # 只接收整数，其它类型返回404
    # path('<int:year>', views.year),
    path('<int:year>/<str:name>', views.name),

    # 正则匹配
    # name可以在模板中引用
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

    # 自定义过滤器
    path('<yyyy:year>', views.year),
]
