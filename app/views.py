from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def portfolio(request):
    return render(request, 'portfolio.html')

def service(request):
    return render(request, 'service.html')

def starter(request):
    return render(request, 'starter.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['Email'] 
        password = request.POST['password']
        password2= request.POST['password2']
    
        if password == password2:
            if User.objects.filter(email=email).exists(): 
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():  
                messages.info(request, 'Username already exists')  
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else: 
            messages.info(request, 'Password do not match') 
            return redirect('register')  
    else:   
        return render(request, 'register.html')
