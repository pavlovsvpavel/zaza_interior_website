from django.db import models
from django.utils.translation import gettext_lazy as _
from zaza_interior.web.validators import validate_phone_number


class ContactFormData(models.Model):
    MAX_LENGTH_FIRST_NAME = 20
    MAX_LENGTH_LAST_NAME = 20
    MAX_PHONE_NUMBER_LENGTH = 15

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        blank=False,
        null=False,
        verbose_name=_("First Name"),
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        blank=False,
        null=False,
        verbose_name=_("Last Name"),
    )
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name=_("Email"),
    )

    phone_number = models.CharField(
        max_length=MAX_PHONE_NUMBER_LENGTH,
        blank=False,
        null=False,
        validators=[
            validate_phone_number,
        ],
        verbose_name=_("Phone number"),
    )

    message = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("Message"),
    )

    created_on = models.DateTimeField(
        auto_now_add=True,

    )

    def __str__(self):
        return f"Submitted form from {self.first_name} {self.last_name}"