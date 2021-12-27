from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password2')

        # Check Passwords
        if password == password_confirm:
            check_username = User.objects.filter(username=username).exists()
            check_email = User.objects.filter(email=email).exists()

            # Check Username
            if check_username:
                messages.error(request, 'Username is already taken')
                return redirect('register')

            if check_email:
                messages.error(request, 'We have already an account registered with this email address')
                return redirect('register')

            new_user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            new_user.save()

            messages.success(request, 'Your account is successfuly created')
            return redirect('login')

        else:
            messages.error(request, 'Paswords must be similars')
            return redirect('register')

    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'We are happy to see you back !')
            return redirect('dashboard')
        
        else:
            messages.error(request, 'Please, try again...')
            return redirect('login')

    return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
