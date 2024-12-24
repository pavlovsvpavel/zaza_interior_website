from django.contrib import admin
from import_export.admin import ExportMixin

from zaza_interior.web.models import ContactFormData


@admin.register(ContactFormData)
class ContactFromDataAdmin(ExportMixin,admin.ModelAdmin):
    list_display = (
        "first_name", "last_name", "email", "phone_number", "message"
    )

    readonly_fields = (
        "first_name", "last_name", "email", "phone_number", "message"
    )
