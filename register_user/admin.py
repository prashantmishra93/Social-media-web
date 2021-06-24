from django.contrib import admin
from .models import RegisterData, Image

# Register your models here.

class RegisterUser(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(RegisterData, RegisterUser)

class ImageUser(admin.ModelAdmin):
    list_display = ('user', 'name', 'address', 'photo', 'date')

admin.site.register(Image, ImageUser)