from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            error_message = 'Passwords do not match. Please enter matching passwords.'
            return render(request, 'register.html', {'error_message': error_message})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different username.'
            return render(request, 'register.html', {'error_message': error_message})

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            error_message = 'Email already registered. Please use a different email.'
            return render(request, 'register.html', {'error_message': error_message})

        # Create the user
        new_user = User.objects.create_user(username=username, email=email, password=password1)
        new_user.first_name = username
        new_user.save()

        messages.success(request, 'Your account has been created successfully!')
        return redirect('authentication:login')

    return render(request, 'register.html', {})


def  Login(request):
    if request.method =='POST':
        username=request.POST.get('fname')
        password=request.POST.get('pwd')
        remember_me=request.POST.get('remember')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            # Implement remember me functionality
            if remember_me:
                # Set a session variable or use Django's built-in remember me feature
                request.session.set_expiry(1209600)  # Two weeks in seconds

            return redirect('home_page:mainpage')   
        
        else:
            return HttpResponse("error. the user does not exist")




    return render(request,'login.html', {})
