from django.contrib import admin
from .models import (
    Categories,
    Post
)

# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    class Meta:
        model = Categories
        fields = ['uuid','name','created_at','updated_at']
    
class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        fields = ['uuid','body','user',"get_categories",'created_at','updated_at']
    
    def get_categories(self,obj):
        ",".join([category.name for category in obj.categories.all()])


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Post, PostAdmin)
