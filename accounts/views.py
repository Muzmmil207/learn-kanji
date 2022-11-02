from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .decorators import is_not_authenticated
from .forms import CustomAuthForm, UserChangeForm, UserRegistrationForm
from .models import User
from .token import account_activation_token

# Create your views here.


@login_required(login_url="login/")
def user_account_settings_view(request):
    form = UserChangeForm(instance=request.user)
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("settings")

    context = {"form": form}
    return render(request, "registration/account-settings.html", context)


@is_not_authenticated
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist.")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("home")
            messages.error(request, "you have not activated your account yet.")
        else:
            messages.error(request, "email or password is incorrect.")
    return render(
        request,
        "registration/login.html",
    )


def logout_view(request):
    logout(request)
    return redirect("login")


@is_not_authenticated
def register_view(request):
    form = UserRegistrationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            # to get the domain of the current site
            current_site = get_current_site(request)

            mail_subject = "Activation link has been sent to your email id"
            message = render_to_string(
                "registration/account-activated.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.id)),
                    "token": account_activation_token.make_token(user),
                },
            )
            to_email = user.email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            messages.success(request, "Account succesfully created. You need to active it.")
            return redirect("login")

    context = {"form": form}
    return render(request, "registration/reqister.html", context)


def verify_account_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account successfully activate. You can now login")
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect("login")
