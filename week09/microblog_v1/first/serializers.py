from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Articles


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):

    # 在序列化器中，将owner设置为只读。
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Articles
        # url是自动生成的。
        fields = ['url', 'id', 'articleid', 'article', 'createtime', 'owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    # 此处自定义一个序列化字段，类似于数据库models中字段的定义方法。
    # 此处获取用户所发文章id列表
    # 这个字段类型是：PrimaryKeyRelatedField
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())

    class Meta:
        model = User
        # 引入所需用户字段。所有字段可在admin界面查询以及管理。
        # url关联的url：也就是进一步访问用户信息/或者访问具体用户信息的api链接。url是自动生成的。
        # articles：详见上述说明。
        fields = ['url', 'id', 'username', 'articles']