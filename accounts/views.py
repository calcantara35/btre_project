from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # check username if already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists! Try again!')
                return redirect('register')
            else:
                # check if email is already being used
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, 'That email is already being used! Try again!')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # import auth from django.contrib
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in!')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in.')
                    return redirect('login')

        else:
            messages.error(
                request, 'Oh no! Passwords do not match! Try Again!')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login User
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
