from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

def HomePage(request):
    return render(request, 'home.html')

def DashBoard(request):
    return render(request, 'dashboard.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Check if email exists, as `authenticate` uses username by default
            user = User.objects.get(email=email)
            username = user.username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Dashboard')
            else:
                return render(request, 'login.html', {'error': 'Invalid email or password'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return render(request, 'signup.html', {'error': "Passwords don't match"})

        if User.objects.filter(username=uname).exists():
            return render(request, 'signup.html', {'error': "Username already exists. Please choose another one."})

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': "Email already exists. Please use a different email address."})

        User.objects.create_user(uname, email, pass1)
        return redirect('Login')
    return render(request, 'signup.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'edit_profile.html', context)