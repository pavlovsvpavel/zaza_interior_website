from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from zaza_interior.gallery.views import LoadImagesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("zaza_interior.web.urls")),
    path("gallery/", include("zaza_interior.gallery.urls")),
    path('load-images/', LoadImagesView.as_view(), name='load_images'),
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
