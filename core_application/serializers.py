from rest_framework import serializers
from .models import (
    Profile,
    Post,
    PostLikes
)
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','date_joined']


class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Profile
        fields = "__all__"

class ProfileLikesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ["user"]

class PostSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    class Meta:
        model = Post
        fields = "__all__"


class PostLikesSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    likes = ProfileLikesSerializer(many=True)
    class Meta:
        model = PostLikes
        fields = "__all__"