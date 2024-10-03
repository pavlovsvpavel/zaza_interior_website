from django.conf import settings
from django.shortcuts import render
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
        context['RECAPTCHA_PUBLIC_KEY'] = settings.RECAPTCHA_PUBLIC_KEY  # Add this line
        return context

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Process form data here, e.g., send an email, save to database, etc.
            # form.cleaned_data['name'], form.cleaned_data['email'], etc.
            return render(request, self.template_name, {'form': form, 'success': True})


        return render(request, self.template_name, {'form': form})


class AboutView(views.TemplateView):
    template_name = "web/about.html"

