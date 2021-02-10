
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bbs import views
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'articles', views.ArticleAPIViewSet)
router.register(r'users', views.UserViewSet )
router.register(r'createusers', views.CreateUserViewSet, 'create-user')
# 适合在现有用户基础上新增字段的情况下使用。
# 手机验证码登陆，现有的模型，序列化，视图会不适用。
# 三方登陆方法，这个视图不适用。
router.register(r'userprofile', views.UserProfileViewSet, 'user-profile')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    path('docs',include_docs_urls(title='BBS')),
]
