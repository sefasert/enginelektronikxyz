from django.shortcuts import render

from django.contrib.sitemaps import views

def sitemap(request, sitemaps, section=None):
    content_type = 'application/xml'
    return views.sitemap(request, sitemaps, section, content_type=content_type)


def error_404(request, exception):
    return render(request, "404.html", {}, status=404)
