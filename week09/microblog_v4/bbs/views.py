from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from .models import Articles, UserScore, Posts
from .serializers import CreateUserSerializer, UserSerializer, ArticlesSerializer, PostsSerializer
from bbs.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework import filters
from django_filters import rest_framework as rf_filters
from .filter import ArticlesFilters

class CreateUserViewSet(viewsets.ModelViewSet):
    """
    创建用户视图
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        """ 
        创建用户 
        """
        serializer = CreateUserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    查看用户视图
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        user = self.get_object()
        # 序列化
        serializer = self.get_serializer(user)
        return Response(serializer.data)

class ArticleAPIViewSet(viewsets.ModelViewSet):
    """
    文章视图
    """
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    filter_backends = (rf_filters.DjangoFilterBackend, filters.SearchFilter,)
    # 增加Django搜索功能,建议使用DRF集成的FilterSet替代
    # https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html#quickstart
    # filter_fields = ('content',)
    filter_class = ArticlesFilters
    search_fields = ['title', 'body']

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user)

class UserPostsAPIViewSet(viewsets.ModelViewSet):
    
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    # def retrieve(self, request, pk=None):
    #     """ 用户详情 """
    #     # 获取实例
    #     postsall = self.get_object()

    #     # 序列化
    #     serializer = self.get_serializer(postsall)
    #     return Response(serializer)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_detail', request=request, format=format),
        'userapi': reverse('user_api', request=request, format=format),
        'articles': reverse('article_list', request=request, format=format),
        'posts': reverse('posts_list', request=request, format=format),
    })

