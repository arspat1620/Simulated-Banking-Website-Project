from django.shortcuts import render,redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def loginV(request):
    if request.user.is_authenticated:
        name = request.user.username
    if request.method=='POST':
        username = request.POST.get('name')
        password = request.POST.get('Pwd')

        user = authenticate(request,username = username, password = password)
        if user is None:
            try:
                user = CustomUser.objects.get(email=username)
            except CustomUser.DoesNotExist:
                try:
                    user = CustomUser.objects.get(PhoneNumber=username)
                except CustomUser.DoesNotExist:
                    return render(request,'login.html',{'error' : "Incorrect Username or Password."})
                else:
                    login(request,user)
                    return redirect('home')
            else:
                login(request,user)
                return redirect('home')
        else:
            login(request,user)
            return redirect('home')
            
    
    try:
        if name:
            return render(request,'login.html',{'name' : name})
    except UnboundLocalError:
        return render(request,'login.html')
    

def register(request):
    if request.user.is_authenticated:
        name = request.user.username
    if request.method=='POST':
        username = request.POST.get('name')
        password = request.POST.get('Pwd')
        email = request.POST.get('email')
        PhoneNumber = request.POST.get('phone')
        confirm_password  = request.POST.get('Con_Pwd')

        if CustomUser.objects.filter(username=username).exists():
            return render(request,'register.html',{'error' : "Username already exists."})
        
        elif password !=confirm_password:
            return render(request,'register.html',{'error' : "Passwords do not match."})
        
        else:
            user = CustomUser.objects.create_user(username = username, password = password, email=email, PhoneNumber = PhoneNumber)
            login(request,user)
            return redirect('home')
        
    try:
        if name:
            return render(request,'register.html',{'name' : name})
    except UnboundLocalError:
        return render(request,'register.html')

def logoutV(request):
    logout(request)
    return redirect('login')