from django.urls import path
from zaza_interior.web.views import IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
)