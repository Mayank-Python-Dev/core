from django.contrib import admin
from .models import (
    Profile,
    Post,
    PostLikes
)

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','created_at','updated_at')

class PostAdmin(admin.ModelAdmin):
    list_display = ('user','caption','created_at','updated_at')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostLikes)