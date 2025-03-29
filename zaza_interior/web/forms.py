from django import forms
from django.utils.translation import gettext_lazy as _
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
                field.widget.attrs['placeholder'] = _('e.g. +359XXXXXXXXX')
                field.label = False
            elif field_name == 'recaptcha':
                continue
            else:
                verbose_name = self.Meta.model._meta.get_field(field_name).verbose_name
                field.widget.attrs["placeholder"] = verbose_name
                field.label = False

    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=True)
