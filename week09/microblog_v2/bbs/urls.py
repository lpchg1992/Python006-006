
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bbs import views
from django.conf.urls import include
# 自动生成文档的工具包。
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'articles', views.ArticleAPIViewSet)
router.register(r'users', views.UserViewSet )
router.register(r'createusers', views.CreateUserViewSet, 'create-user')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    # 自动生成文档。当访问该路由即可访问对应文档。
    path('docs',include_docs_urls(title='BBS')),
]
