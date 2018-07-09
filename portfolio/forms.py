from django import forms


class MessageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    message = forms.CharField(max_length=250)
