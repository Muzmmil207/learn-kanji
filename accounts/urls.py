from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path

from . import views

urlroutes = [
    path("settings/", views.user_account_settings_view, name="settings"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path(
        "activate-account/<path:uidb64>/<path:token>/", views.verify_account_view, name="activate"
    ),
    path("password/", PasswordResetView.as_view(), name="reset-password"),
    path("password-reset-done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
