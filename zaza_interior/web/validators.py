from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone_number(value):
    if not value.startswith('+') or not value[1:].isdigit() or len(value) < 9 or len(value) > 15:
        raise ValidationError(_("Enter a valid phone number."))

