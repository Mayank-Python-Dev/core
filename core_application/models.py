from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True

"""
CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.
RESTRICT: (introduced in Django 3.1) Similar behavior as PROTECT that matches SQL's RESTRICT more accurately. (See django documentation example)
SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.
SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.
SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.
DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION
"""


class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(null=True,blank=True,default="")

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.user.username


class Post(BaseModel):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    caption = models.TextField(null=True,blank=True,default="")

    class Meta:
        verbose_name_plural = "Post"
    
    def __str__(self):
        return "{}---{}".format(self.user.user.username,self.caption)

class PostLikes(BaseModel):
    post = models.OneToOneField(Post,on_delete=models.CASCADE)
    likes = models.ManyToManyField(Profile,help_text="")

    class Meta:
        verbose_name_plural = "Likes"
