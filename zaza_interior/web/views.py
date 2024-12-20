from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.translation import get_language
from django.views import generic as views
from zaza_interior.web.forms import ContactForm


class IndexView(views.TemplateView):
    template_name = "web/index.html"

class HowItWorksView(views.TemplateView):
    template_name = "web/how-it-works.html"

class ContactsView(views.FormView):
    template_name = "web/contacts.html"
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['RECAPTCHA_PUBLIC_KEY'] = settings.RECAPTCHA_PUBLIC_KEY

        return context

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
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

                return self.render_to_response(self.get_context_data(form=form, success=True))

            except Exception as e:
                return HttpResponse(f"Error sending email: {e}")



        return render(request, self.template_name, {'form': form})


class AboutView(views.TemplateView):
    template_name = "web/about.html"

