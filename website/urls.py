from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('xavier/', admin.site.urls),
    path('', include('authentication.urls', namespace='authentication')),
    path('portpolio/', include('portpolio.urls', namespace='portpolio')),
]
