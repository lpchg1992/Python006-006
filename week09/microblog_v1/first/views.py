from django.shortcuts import render

# Create your views here.


from .models import Articles
from .serializers import ArticlesSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from first.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from first.serializers import UserSerializer
from rest_framework.decorators import api_view


# 关于ModelViewSet具体可查看相关代码。是基于GenericViewSet以及各种mixin的封装。
class ArticleAPIViewSet(viewsets.ModelViewSet):
    """
    使用serializers和viewset
    """
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    # 具体查看相关代码。可以配置不同请求方式的许可方式以及权限。
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    # 是针对CreateModelMixin中方法的改写。
    # 是create方法之后进行保存的步骤。
    def perform_create(self, serializer):
        # 对用户进行关联的保存操作。
        serializer.save(owner=self.request.user)

# 只读视图。
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 由DefaultRouter中的root_view_name='api-root'对应功能进行调用。
# 也就是，当访问api根目录会调用如下函数。
# 接收视图可以被请求的方法，此处为get，如果需要支持其他参数，可以在GET后面添加方法。
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 通过注册的url名称，取出对应的url。
        'users': reverse('user-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format)
    })

