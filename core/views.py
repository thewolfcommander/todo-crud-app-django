from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login
from django.contrib.auth.decorators import login_required

from core import forms
from core import models

@login_required
def home(request):
    active_tasks = models.Task.objects.filter(active=True, owner=request.user)
    inactive_tasks = models.Task.objects.filter(active=False, owner=request.user)
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
        'active': active_tasks,
        'inactive': inactive_tasks,
    }
    return render(request, 'core/home.html', context)

@login_required
def update(request, id=None, *args, **kwargs):
    obj = get_object_or_404(models.Task, id=id)
    if obj.owner == request.user:
        if obj.active == True:
            obj.active = False
            obj.save()
            return redirect('home')
        else:
            obj.active = True
            obj.save()
            return redirect('home')
    else:
        return redirect('home')

@login_required
def delete(request, id=None, *args, **kwargs):
    obj = get_object_or_404(models.Task, id=id)
    if obj.owner == request.user:
        obj.delete()
        return redirect('home')
    else:
        return redirect('home')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = forms.SignUpForm(request.POST or None)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_staff = True
                user.save()
                auth_login(request, user)
                return redirect('home')
        else:
            form = forms.SignUpForm()
        context = {
            'form': form,
        }
        return render(request, 'signup.html', context)