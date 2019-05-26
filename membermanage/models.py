from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']