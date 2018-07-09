# core django
from django.forms import ModelForm

# project
from .models import Message


class MessageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
