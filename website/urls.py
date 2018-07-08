# core django
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('authentication.urls', 'authentication'),
                     namespace='authentication')),
    re_path(r'^$', lambda r: HttpResponseRedirect('portfolio/')),
    path('portfolio/', include(('portfolio.urls', 'portfolio'), namespace='portfolio')),
]
