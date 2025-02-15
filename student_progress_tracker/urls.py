"""
URL configuration for student_progress_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# student_progress_tracker/urls.py
from django.contrib import admin
from django.urls import path, include
from tracker.views_csp import robots_txt, sitemap_xml  # Import the views from tracker

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),  # Include the tracker app URLs
    path('robots.txt', robots_txt),     # Serve robots.txt with CSP headers
    path('sitemap.xml', sitemap_xml),   # Serve sitemap.xml with CSP headers
]
