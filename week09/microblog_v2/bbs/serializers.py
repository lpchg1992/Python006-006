from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Articles
# 当需要校验密码，可以将明文密码和加密密码进行比对。
from django.contrib.auth.hashers import make_password, check_password

class ArticlesSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Articles
        fields = ['id', 'articleid', 'article', 'createtime', 'owner', 'title']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username','articles']

class CreateUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        # exclude = ('password',)
        fields = ['url', 'id', 'username', 'email', 'password']

    
    def validate(self, attrs):
 		# 对密码进行加密 make_password，这个是django自带的方法。
        attrs['password'] = make_password(attrs['password'])
        return attrs