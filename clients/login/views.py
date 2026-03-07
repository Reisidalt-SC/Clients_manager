from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.validators import validate_email
from django.core.exceptions import ValidationError





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/clients')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login/login.html', {'error_message': error_message})
    return render(request, 'login/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

            #validate username and email uniqueness
        if User.objects.filter(username=username).exists():
            return render(request, 'login/register.html', {'error_message': 'Username already exists.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'login/register.html', {'error_message': 'Email already exists.'})

            #validate email format
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'login/register.html', {'error_message': 'Invalid email format.'})
        

        #user creation
        User.objects.create_user(username=username, email=email, password=password) 
        return redirect('/clients') 
    return render(request, 'login/register.html')