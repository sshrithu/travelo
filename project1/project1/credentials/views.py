from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):

    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        password=request.POST['password']
        cnfpassword=request.POST['password1']
        email=request.POST['email']
        if password==cnfpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('register')
            else:
                 user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
                 user.save()
                 # print("user registered")
                 return redirect('login')

        else:
            messages.info(request,"password mismatch")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')