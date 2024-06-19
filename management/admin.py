from django.contrib import admin
from .models import (
    Professions,
    Profile
)
from django.utils import timezone

# Register your models here.

class ProfessionAdmin(admin.ModelAdmin):
    class Meta:
        model = Professions


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username','email','birthday','age']
    exclude = ['username','email']

    class Meta:
        model = Profile
    
    def age(self,profile):
        return int((timezone.now().date() - profile.birthday).days // (365.25))
    
        


admin.site.register(Professions,ProfessionAdmin)
admin.site.register(Profile,ProfileAdmin)