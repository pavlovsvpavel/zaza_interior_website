from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic as views
from zaza_interior.web.forms import ContactFormCreate
from zaza_interior.web.models import ContactFormData


class IndexView(views.TemplateView):
    template_name = "web/index.html"


class HowItWorksView(views.TemplateView):
    template_name = "web/how-it-works.html"


class ContactsView(views.CreateView):
    model = ContactFormData
    template_name = "web/contacts.html"
    form_class = ContactFormCreate
    success_url = reverse_lazy('contacts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def form_valid(self, form):
        self.object = form.save()

        subject = "ZazaInterior New Contact Form"

        email_content = render_to_string('web/email_template.html', {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email'],
            'phone_number': form.cleaned_data['phone_number'],
            'message': form.cleaned_data['message'],
        })

        from_email = form.cleaned_data['email']
        recipient_list = [settings.DEFAULT_FROM_EMAIL]

        try:
            email = EmailMessage(
                subject, email_content, from_email, recipient_list
            )
            email.content_subtype = "html"
            email.send(fail_silently=False)

        except Exception as e:
            return HttpResponse(f"Error sending email: {e}")

        return self.render_to_response(self.get_context_data(form=form, success=True))


class AboutView(views.TemplateView):
    template_name = "web/about.html"
