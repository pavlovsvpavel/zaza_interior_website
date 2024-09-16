from django.views import generic as views

class IndexView(views.TemplateView):
    template_name = "web/index.html"

class HowItWorksView(views.TemplateView):
    template_name = "web/how-it-works.html"


class ContactsView(views.TemplateView):
    template_name = "web/contacts.html"

class AboutView(views.TemplateView):
    template_name = "web/about.html"

