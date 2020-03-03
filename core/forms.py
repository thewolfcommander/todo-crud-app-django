from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core import models

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs = {'class': 'materialize-textarea'}))
    class Meta:
        model = models.Task
        fields = ['title', 'description']