from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from .forms import CustomAuthenticationForm  # If using CustomAuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# User Registration View
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            messages.success(request, 'Account created successfully! You are now logged in.')
            return redirect('profile')  # Redirect to the profile page after successful registration
        else:
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

# User Login View
def login_page(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.email}!')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'There was an error with your login credentials.')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})



# User Profile View (Requires login)
@login_required
def profile(request):
    return render(request, 'index.html')
def user(request):
    return render(request, 'user.html')

# User Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
