# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from .models import Articles, UserProfile
from django.contrib.auth.hashers import make_password, check_password

class ArticlesSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Articles
        fields = ['id', 'articleid', 'article', 'createtime', 'owner', 'title']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    # other = OtherSerializer(read_only=True, many=True)
    # class Meta:
    #     fields = (..., 'other',)
    
    class Meta:
        model = UserProfile
        fields = ['username', 'nickname', 'phone_number', 'description', 'createtime', 'score']



class UserSerializer(serializers.HyperlinkedModelSerializer):


    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())

    profiles = ProfileSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'articles', 'profiles']





class CreateUserSerializer(serializers.HyperlinkedModelSerializer):

    profiles = ProfileSerializer(many=True)


    class Meta:
        model = User
        # exclude = ('password',)
        fields = ['url', 'id', 'username', 'email', 'password', 'profiles']

    
    def validate(self, attrs):
 		# 对密码进行加密 make_password
        attrs['password'] = make_password(attrs['password'])
        return attrs