from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            email_data = request.POST['email']
            
            newuser = User.objects.create_user(
                username=email_data,
                password=request.POST['password'],
            )
            nickname = request.POST['nickname']
            profile = Profile(
                user=newuser,
                nickname=nickname,
            )
            profile.save()
            
            auth.login(request, newuser)
            return redirect('main:onboarding')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        email_data = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=email_data, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main:onboarding')
        else:
            return render(request, 'accounts/login.html')
            
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('main:onboarding')