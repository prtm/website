from django.shortcuts import render
from django.http import Http404

# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'portfolio/home.html')

    return Http404('Error Page Not Found!')
