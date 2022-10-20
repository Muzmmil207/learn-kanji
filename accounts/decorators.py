from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def is_not_authenticated(function):
    @wraps(function)
    def wrap(request, *args):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return function(request, *args)

    return wrap


def is_active(function):
    @wraps(function)
    def wrap(request, *args):

        if request.user.is_active:
            return function(request, *args)
        else:
            messages.error(request, "Your account hasn't been verified")
            return redirect("verify")

    return wrap
