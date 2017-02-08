from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.template.context import RequestContext


# Create your views here.


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/user/login')


@login_required(login_url='/user/login')
def home(request):
    return render(request, 'home.html')

