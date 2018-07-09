# stdlib
import requests
import json

# core django
from django.contrib import messages
from django.shortcuts import render
from django.http import Http404

# project
from .forms import MessageForm
from .helper import get_client_ip
from website.settings.base import get_secret

# Create your views here.


reCAPTCHA_secret = get_secret('reCAPTCHA_secret')


def home(request):
    if request.method == 'POST':
        # Form was submitted
        form = MessageForm(request.POST)
        scroll_to_bottom = True
        if form.is_valid():
            # Form fields passed validation
            # verify recaptcha3
            token = request.POST.get('token')
            client_ip = get_client_ip(request)
            # print(request.POST, reCAPTCHA_secret, token, client_ip)
            if token is not None:
                if client_ip is not None:
                    post_data = {'secret': reCAPTCHA_secret,
                                 'response': token, 'remoteip': client_ip}
                else:
                    post_data = {'secret': reCAPTCHA_secret,
                                 'response': token}

                response = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify', data=post_data)
                # print(response, response.content)
                response_body = json.loads(response.content.decode('utf-8'))
                if(response_body.get('success')):
                    form.save()
                    messages.success(request, 'Submission successful')
                    form = MessageForm()
            else:
                messages.error(request, 'Recaptcha error')

    else:
        scroll_to_bottom = False
        form = MessageForm()

    return render(request, 'portfolio/home.html', {'form': form, 'scroll_to_bottom': scroll_to_bottom})
