from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'(?P<search>^[\u4E00-\u9FFF]*.*)', views.show_comments),
]
