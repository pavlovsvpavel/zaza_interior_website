from django.urls import path
from zaza_interior.web.views import IndexView, ContactsView, AboutView, HowItWorksView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
    path("how-it-works/", HowItWorksView.as_view(), name="how-it-works"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("about/", AboutView.as_view(), name="about"),
)