from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login

from core import forms

def home(request):
    return render(request, 'core/home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = forms.SignUpForm(request.POST or None)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('home')
        else:
            form = forms.SignUpForm()
        context = {
            'form': form,
        }
        return render(request, 'signup.html', context)