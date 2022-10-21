from django.contrib import admin
from django.urls import path, include
from accounts.urls import urlroutes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kanji.urls')),
    
    # Third part app
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += urlroutes
