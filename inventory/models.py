import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Brand(BaseModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Brand"
    
    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Product(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    categories = models.ManyToManyField(Category)
    price = models.FloatField()

    class Meta:
        verbose_name_plural = "Product"
    
    def __str__(self):
        return self.name

class Order(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.product.name



