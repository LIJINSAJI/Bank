from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def message(request):
    return render(request,'message.html')

def user(request):
    return render(request,'user.html')

def accform(request):
    if request.method == 'POST':
        form = accform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully",{'form': form})
    return render(request,'accform.html')

def login(request):
    if request.method=='POST':
        Username = request.POST['username']
        Password = request.POST['password']
        User=auth.authenticate(username=Username,password=Password)
        if User is not None:
            auth.login(request,User)
            return redirect('user')
        else:
            messages.info(request,"invalid user")
            return redirect(request,'login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        Username = request.POST['username']
        Email = request.POST['email']
        Password = request.POST['password']
        ConfirmPassword = request.POST['confirm_password']
        if Password==ConfirmPassword:
            if User.objects.filter(username=Username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=Username,password=Password,email=Email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')