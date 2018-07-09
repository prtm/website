# core django
from django.contrib import messages
from django.shortcuts import render
from django.http import Http404

# project
from .forms import MessageForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        # Form was submitted
        form = MessageForm(request.POST)
        scroll_to_bottom = True
        if form.is_valid():
            # Form fields passed validation
            form.save()
            form = MessageForm()
            messages.success(request, 'Submission successful')
    else:
        scroll_to_bottom = False
        form = MessageForm()

    return render(request, 'portfolio/home.html', {'form': form, 'scroll_to_bottom': scroll_to_bottom})
