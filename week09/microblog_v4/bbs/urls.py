
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bbs import views
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls


# 功能     路径             方式
# 创建用户  /usersapi/   POST
# 查看用户  /users/         GET
# 创建文章  /articles       POST
# 查看文章  /articles       GET
# 评论文章  /posts/         POST
# 查看评论  /articles       GET


router = DefaultRouter()
router.register(r'users', views.UserViewSet )
router.register(r'usersapi', views.CreateUserViewSet, 'user_api')
router.register(r'articles', views.ArticleAPIViewSet, 'articles_list')
router.register(r'posts', views.UserPostsAPIViewSet, 'posts_list')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    path('docs',include_docs_urls(title='BBS')),
]
