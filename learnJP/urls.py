from accounts.urls import urlroutes
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("kanji.urls")),
    path("api/", include("api.urls")),
    # Third part app
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += urlroutes
