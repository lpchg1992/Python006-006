# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from .models import Articles, Posts
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view



class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    """文章序列"""
    author_id = serializers.ReadOnlyField(source='author_id.username')

    class Meta:
        model = Articles
        fields = ['id', 'author_id', 'body', 'create_time', 'title']

# class ProfileAPISerializer(serializers.HyperlinkedModelSerializer):
#     """用户积分序列"""
#     lookup_field = 'id'
#     class Meta:
#         model = ProfileAPI
#         fields = ['url','score', 'owner']
#     extra_kwargs = {
#         'url': {'lookup_field': 'id'},
#         'owner': {'lookup_field': 'id'}
#         }



class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    """创建用户序列"""

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', ]
    
    def validate(self, attrs):
 		# 对密码进行加密 
        attrs['password'] = make_password(attrs['password'])
        return attrs

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """用户序列"""
    # articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())
    articles = ArticlesSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'articles', ]


class PostsSerializer(serializers.ModelSerializer):
    """评论序列"""
 
    class Meta:
        model = Posts
        fields = ['id', 'content', 'create_time', 'article_id', 'user_id']

    @api_view(['GET'])
    def showdata(request):
        id = request.GET['id']
        datas=Posts.objects.filter(article_id=id)
        postdata = PostsSerializer(datas,many=True)
        return Response({'data':PostsSerializer.data})

