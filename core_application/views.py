from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import (
    status
)
from .models import (
    Profile,
    Post,
    PostLikes
)
from .serializers import (
    ProfileSerializer,
    PostSerializer,
    PostLikesSerializer
)

# Create your views here.

class ProfileView(APIView):
    def get(self, request, *args, **kwargs):
        get_profile = Profile.objects.select_related("user")
        serializer = ProfileSerializer(get_profile, many=True)
        context = {
            "status": status.HTTP_200_OK,
            "success": True,
            "response": serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

class PostView(APIView):
    def get(self, request, *args, **kwargs):
        get_post = Post.objects.prefetch_related("user__user")
        serializer = PostSerializer(get_post, many=True)
        context = {
            "status": status.HTTP_200_OK,
            "success": True,
            "response": serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class PostLikesView(APIView):
    def get(self, request, *args, **kwargs):
        get_post_likes = PostLikes.objects.select_related("post__user").prefetch_related("likes__user")
        serializer = PostLikesSerializer(get_post_likes, many=True)
        context = {
            "status": status.HTTP_200_OK,
            "success": True,
            "response": serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)