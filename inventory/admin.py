from django.contrib import admin
from .models import (
    Brand,
    Category,
    Product,
    Order
)

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ['uuid','name','created_at','updated_at']
    class Meta:
        model = Brand
        # fields = "__all__"
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['uuid','name','created_at','updated_at']
    class Meta:
        model = Category
        # fields = "__all__"

class ProductAdmin(admin.ModelAdmin):
    list_display = ['uuid','brand','name','get_categories','price','created_at','updated_at']
    class Meta:
        model = Product
        # fields = "__all__"
    
    def get_categories(self, obj):
        print(obj)
        return ",".join([category.name for category in obj.categories.all()])


class OrderAdmin(admin.ModelAdmin):
    list_display = ['uuid','customer','product','quantity','total_price','created_at','updated_at']
    class Meta:
        model = Order
        # fields = "__all__"
    
    def total_price(self, obj):
        return obj.quantity * obj.product.price

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
