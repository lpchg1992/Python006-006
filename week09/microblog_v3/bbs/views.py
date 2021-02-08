from django.shortcuts import render

# Create your views here.


from .models import Articles, UserProfile
from .serializers import ArticlesSerializer
from rest_framework import viewsets, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from bbs.permissions import IsOwnerOrReadOnly
# from django.contrib.auth.models import 
from django.contrib.auth import get_user_model
User = get_user_model()
from bbs.serializers import UserSerializer, CreateUserSerializer, ProfileSerializer
from rest_framework.decorators import api_view

class ArticleAPIViewSet(viewsets.ModelViewSet):
    """
    使用serializers和viewset
    """
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CreateUserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        user = self.get_object()

        # 序列化
        serializer = self.get_serializer(user)
        data = serializer.data
        del data['password']
        return Response(data)

    def list(self, request: Request, *args, **kwargs):
        """ 获取用户列表 """
        return Response([])


    def create(self, request, *args, **kwargs):
        """ 
        创建用户 
        """
        
        serializer = CreateUserSerializer(data=request.data, context={'request': request})
        # print(request.data['username'])
        # save 前必须先调用 is_valid()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    # def update(self, request: Request, *args, **kwargs):
    #     """ 
    #     更新用户信息 
    #     """

    # def destroy(self, request: Request, *args, **kwargs):
    #     """ 
    #     删除用户 
    #     """
    #     serializer = self.get_serializer(self.queryset, many=True)
    #     return Response(serializer.data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        user = self.get_object()

        # 序列化
        serializer = self.get_serializer(user)
        return Response(serializer.data)


    # def list(self, request: Request, *args, **kwargs):
    #     """ 获取用户列表 """


class UserProfileViewSet(viewsets.ModelViewSet):
    
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        userprofile = self.get_object()

        # 序列化
        serializer = self.get_serializer(userprofile)
        return Response(serializer)

    def list(self, request: Request, *args, **kwargs):
        """ 获取用户详细信息 """
        return Response([])


    def create(self, request, *args, **kwargs):
        """ 
        创建用户 
        """
        
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        # print(request.data['username'])
        # save 前必须先调用 is_valid()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-detail', request=request, format=format),
        'createusers': reverse('create-user', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format),
        'userprofile': reverse('user-profile', request=request, format=format),
    })

