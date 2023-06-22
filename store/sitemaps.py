from django.contrib.sitemaps import Sitemap

from .models import Product

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    protocol = "https"

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        urls = []
        absolute_url = obj.get_absolute_url()
        urls.append(f'http://{absolute_url}')
        urls.append(f'https://{absolute_url}')
        return urls

    def lastmod(self, obj):
        return obj.created_date
