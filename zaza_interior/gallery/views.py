from django.views import generic as views
from filer.models.imagemodels import Image


class MainGalleryView(views.TemplateView):
    template_name = "gallery/main_gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["images"] = Image.objects.all()

        return context