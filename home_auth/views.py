from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
# Create your views here.
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # handle existing user case
        if CustomUser.objects.filter(email= email).exists():
            return render(request, 'authentication/register.html', {'error': 'Email already in use. Please sign up with a different email or login.'})

        # Handle password mismatch
        if password != confirm_password:
            return render(request, 'authentication/register.html', {'error': 'Passwords do not match.'})

        # create user logic goes here
        user = CustomUser.objects.create_user(  # create_user is a method provided by AbstractUser (ensure password is hashed & default fields are handled -> create won't work here)
            # username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        login(request, user)
        return redirect('student_list')     # redirect to dashboard later based on user role
    return render(request, 'authentication/register.html')

from django.contrib.auth import authenticate
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password) # get the authenticated user object
        if user is not None:
            login(request, user)
            return redirect('student_list')  # redirect to dashboard later based on user role
        return render(request, 'authentication/login.html', {'error': 'Invalid email or password.'})

    return render(request, 'authentication/login.html')

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']   # assume email is sent via POST
        user = CustomUser.objects.get(email=email)   # as email is unique
        if user:
            pass           
            
        return render(request, 'authentication/forgot-password.html', {'error': 'User doesn\'t exist.'})
        

        # Here, you would typically generate a password reset token and send an email to the user.
        # For simplicity, we'll just render a success message.
        return render(request, 'authentication/forgot-password.html', {'message': 'A password reset link has been sent to your email.'})
    return render(request, 'authentication/forgot-password.html')