from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import User
from .forms import UserRegistrationForm, CustomAuthForm, UserChangeForm
# Create your views here.


def user_account_settings_view(request):

    form = UserChangeForm(instance=request.user)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('settings')

    context = {'form': form}
    return render(request, 'registration/account-settings.html', context)


def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'email or password is incorrect.')
    return render(request, 'registration/login.html', )


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account succesfully created. You can now login')
            return redirect('login')

    context = {'form': form}

    return render(request, 'registration/reqister.html', context)
