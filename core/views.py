from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login
from django.contrib.auth.decorators import login_required

from core import forms
from core import models

@login_required
def home(request):
    active_tasks = models
    if request.method == 'POST':
        form = forms.TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('home')
    else:
        form = forms.TaskForm()
    context = {
        'form': form,
    }
    return render(request, 'core/home.html', context)


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