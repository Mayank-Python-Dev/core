from typing import Any, Mapping
from django.contrib import admin
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import (
    Category,
    Product,
    Order
)
from django.forms import ModelForm

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['uuid','name','created_at','updated_at']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['uuid','name','get_categories','price','is_available','quantity','created_at','updated_at']

    def get_categories(self, obj):
        return "\n".join([category.name for category in obj.categories.all()])

class OrderForm(ModelForm):
    class Meta:
        models = Order
    
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        if self.instance.uuid:
            self.fields['product'].queryset = Product.objects.filter(is_available=True)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['uuid','customer','product','quantity','created_at','updated_at']
    form = OrderForm


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)