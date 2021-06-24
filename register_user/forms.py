from django import forms
from .models import RegisterData, Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Getform(forms.ModelForm):
    class Meta:
        model = RegisterData
        fields = ('username', 'email', 'password')

class Imageform(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
