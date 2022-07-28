from asyncio import log
import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.


def signup_func(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #login user
            user = form.save()
            login(request, user)
            return redirect('/actors/')
    else:
        form  = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_func(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('/actors/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_func(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/actors/')