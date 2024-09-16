from django.urls import path
from zaza_interior.gallery.views import MainGalleryView, LoadImagesView

urlpatterns = (
    path("", MainGalleryView.as_view(), name="main_gallery"),
)