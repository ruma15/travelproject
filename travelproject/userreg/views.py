from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid user")
            return redirect('login')

    return render(request,"login.html")

# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['Password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name already taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, email=email, first_name=firstname,
                                                last_name=lastname, password=password)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "Password not matched")
            return redirect('registration')
        return redirect('login')
    return render(request, "registration.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
