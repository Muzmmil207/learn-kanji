from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("characters/", views.characters_view, name="all_chars"),
    path("characters/<str:letter>/", views.character_view, name="char"),
]
