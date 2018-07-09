from django.contrib import messages
from django.shortcuts import render
from django.http import Http404


# project
from .forms import MessageForm

# Create your views here.


def home(request):
    scroll_to_bottom = False
    if request.method == 'POST':
        # Form was submitted
        form = MessageForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            form = MessageForm()
            messages.success(request, 'Submission successful')
        else:
            scroll_to_bottom = True
    else:
        form = MessageForm()

    return render(request, 'portfolio/home.html', {'form': form, 'scroll_to_bottom': scroll_to_bottom})
