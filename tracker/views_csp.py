from django.http import HttpResponse
from django.views.decorators.http import require_GET

@require_GET
def robots_txt(request):
    content = "User-agent: *\nDisallow: /admin/\n"
    response = HttpResponse(content, content_type="text/plain")
    response['Content-Security-Policy'] = "default-src 'self'"
    return response

@require_GET
def sitemap_xml(request):
    content = "<?xml version='1.0' encoding='UTF-8'?>\n<urlset></urlset>"
    response = HttpResponse(content, content_type="application/xml")
    response['Content-Security-Policy'] = "default-src 'self'"
    return response
