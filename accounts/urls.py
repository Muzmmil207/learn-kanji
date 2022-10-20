from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.user_account_settings_view, name="settings"),

]
