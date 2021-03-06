from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order import views
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls

# DefaultRouter是SimpleRouter的扩展。
# 新增一个root_view_name参数。
router = DefaultRouter()
router.register(r'orders/create', views.OrderCreateViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs', include_docs_urls(title='Order'))
]