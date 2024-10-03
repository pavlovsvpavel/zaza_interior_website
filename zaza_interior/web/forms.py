from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible, ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={
        'class': 'input',
        'id': 'first-name',
    }))

    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={
        'class': 'input',
        'id': 'last-name',
    }))

    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={
        'class': 'input',
        'id': 'email',
    }))

    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={
        'class': 'input',
        'id': 'phone-number',
    }))

    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'class': 'textinput',
        'id': 'message',
        'placeholder': 'Please enter your message...',
        'style': 'resize: none;',
    }))

    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
