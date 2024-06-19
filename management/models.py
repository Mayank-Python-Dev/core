from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Professions(BaseModel):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Computers and information technology"

class Profile(BaseModel):
    username = models.CharField(max_length=256, null=True, blank=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, null=True, blank=True)
    birthday = models.DateField(editable=True)
    address = models.TextField()
    position = models.ForeignKey(Professions,on_delete=models.CASCADE, related_name="position")

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.username = self.first_name[0] + self.last_name
        self.email = self.first_name[0] + self.last_name + "@company.com"
        super(Profile, self).save(*args, **kwargs)
