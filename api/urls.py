from django.urls import path

from .views import CharacterAPIView

urlpatterns = [path("<int:num>/", CharacterAPIView.as_view(), name="character_api")]
