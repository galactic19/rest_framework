from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post


class PostOption(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk', 'username', 'email']


class PostSerializer(ModelSerializer):
    # author = PostOption()
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = [
            'pk',
            'author_name',
            'content',
            'created_at',
            'updated_at',
            'is_public',
        ]