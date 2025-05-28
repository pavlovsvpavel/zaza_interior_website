from django.contrib import admin
from django.contrib.sites.models import Site
from import_export.admin import ExportMixin

from zaza_interior.web.models import ContactFormData


@admin.register(ContactFormData)
class ContactFromDataAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        "first_name", "last_name", "email",
        "phone_number", "message", "created_on",
    )

    readonly_fields = (
        "first_name", "last_name", "email",
        "phone_number", "message", "created_on",
    )


admin.site.unregister(Site)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("id", "domain", "name")
    search_fields = ("id", "domain", "name")
