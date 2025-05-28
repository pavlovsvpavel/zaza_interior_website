from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['index', 'how-it-works', 'contacts', 'about']

    def location(self, item):
        return reverse(item)

class GalleryViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['main_gallery']

    def location(self, item):
        return reverse(item)
