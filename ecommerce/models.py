import uuid 
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Category"
    
    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=256)
    categories = models.ManyToManyField(Category, related_name="category", help_text="Product Category List")
    price = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1, validators = [MinValueValidator(0)])

    class Meta:
        verbose_name_plural = "Product"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.quantity <= 0:
            self.is_available = False
        super(Product, self).save(*args, **kwargs)

class Order(BaseModel):
    customer = models.ForeignKey(User, related_name="customer", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="customer_product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators = [MinValueValidator(0)])

    class Meta:
        verbose_name_plural = "Order"
    
    def __str__(self):
        return "{} -- {}".format(self.customer.username, self.product.name)
    
    def clean(self, *args, **kwargs):
        get_product_instance = get_object_or_404(Product, uuid = self.product.uuid)
        if get_product_instance.quantity <= self.quantity:
            raise ValidationError(
                f"We have only { get_product_instance.quantity } { get_product_instance.name} Available"
            )
        return super(Order, self).clean(*args, **kwargs)

