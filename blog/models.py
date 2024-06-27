import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

   
class Categories(BaseModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(BaseModel):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    categories = models.ManyToManyField(Categories)
    
    class Meta:
        verbose_name_plural = "Post"
    
    def __str__(self):
        return "{} -- {}...".format(self.user.username, self.body[:20])
