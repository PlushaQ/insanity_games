from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import re

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect("homepage")
        else:
            return render(request, 'login.html', {'error': "Username or password is invalid."})

    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("homepage")
    return render(request, 'logout.html')


def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            if not re.match(r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*\W).{8,}$", request.POST['password']):
                return render(request, 'signup.html',
            {'error': "Your password should be at least 8 characters and cointans 1 letter, 1 number and 1 symbol."})
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': "User with that name already exists."})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'signup.html', {'error': "Passwords don't match ."})

    else:

        return render(request, 'signup.html')