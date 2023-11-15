from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from . models import *
# from . models import logn
from . models import regs


# Create your views here
def user_login(request):
    if request.method == 'POST':
        # Get the username and password from the form
        user_name = request.POST['user_name']
        password = request.POST['password']
        print(user_name,password)
        # Authenticate the user using your custom model
        user = authenticate(request, user_name=user_name, password=password)
        print("User authenticated:", user)
        if user is not None:
            # If the user is authenticated, log them in
            login(request, user)
            # Redirect to a success page or wherever you want
            return redirect('/')
        else:
            # If authentication fails, display an error message
            error_message = "Invalid username or password."
            return redirect('user_login')
    else:
        return render(request, 'login.html')
       



def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('user_name')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        hashed_pass = make_password(password1)
        if password1==password2:
            obj=regs(user_name=user_name,password=hashed_pass,email=email,first_name=first_name,last_name=last_name)
            obj.save()
            print("user created")
        else:
            print("password not matched")
        return redirect('/')
    else:
        
        return render(request,'registration.html')