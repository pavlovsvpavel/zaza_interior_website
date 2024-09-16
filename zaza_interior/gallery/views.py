from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import generic as views
from easy_thumbnails.files import get_thumbnailer
from filer.models.imagemodels import Image


class MainGalleryView(views.TemplateView):
    template_name = "gallery/main_gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Option 1: Load no images on initial load (rely entirely on infinite scroll)
        context["images"] = []

        # Option 2: Load the first set of images (initial page load with some images)
        # images = Image.objects.all()[:6]
        # context["images"] = images

        return context

class LoadImagesView(views.View):

    def get(self, request, *args, **kwargs):
        images = Image.objects.all().order_by('-date_taken')
        page_number = request.GET.get('page', 1)
        paginator = Paginator(images, 20)
        page_obj = paginator.get_page(page_number)

        images_list = []
        for image in page_obj:
            thumbnail_options = {'size': (200, 150), 'crop': True}
            thumbnail_url = get_thumbnailer(image).get_thumbnail(thumbnail_options).url
            images_list.append({
                'thumbnail_url': thumbnail_url,
                'full_size_url': image.url,
                'alt': image.name or "No name"
            })

        return JsonResponse({
            'images': images_list,
            'has_next': page_obj.has_next(),
        })