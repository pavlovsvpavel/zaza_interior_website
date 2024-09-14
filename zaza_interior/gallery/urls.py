from django.urls import path
from zaza_interior.gallery.views import MainGalleryView

urlpatterns = (
    path("", MainGalleryView.as_view(), name="main_gallery"),
)