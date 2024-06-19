from django.urls import path
from .views import (
    ProfileView,
    PostView,
    PostLikesView
)

urlpatterns = [
    path("user_profile/", ProfileView.as_view(), name="user-profile"),
    path("user_post/", PostView.as_view(), name="user-post"),
    path("user_post_likes/", PostLikesView.as_view(), name="user-post-likes")
]