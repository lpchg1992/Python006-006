from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello django")


#  path('<int:year>', views.year),
def year(request, year):
    return HttpResponse(year)
    # return redirect('/2020.html')


# path('<int:year>/<str:name>', views.name),
# 接收不定长的参数
def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


# re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
# path('<myint:year>', views.year),
def myyear(request, year):
    return render(request, 'yearview.html')
