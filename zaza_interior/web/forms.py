from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from zaza_interior.web.models import ContactFormData


class ContactFormCreate(forms.ModelForm):
    class Meta:
        model = ContactFormData
        fields = ("first_name", "last_name", "email", "phone_number", "message",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'phone_number':
                field.widget.attrs['placeholder'] = 'e.g. +359888123456'
            else:
                field.widget.attrs['placeholder'] = f"Enter your {field_name.replace('_', ' ')}"


    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
