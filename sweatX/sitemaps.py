from django.contrib.sitemaps import Sitemap
from products.models import Product  # <--- FIXED THIS LINE
from django.urls import reverse

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        # If your Product model has an 'updated_at' field, use it here
        return obj.updated_at if hasattr(obj, 'updated_at') else None

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'reviews', 'products'] # Names from your urls.py

    def location(self, item):
        return reverse(item)