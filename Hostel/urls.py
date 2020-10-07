"""Hostel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
import re
from urllib.parse import urlsplit
from django.conf.urls.static import static

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.urls import re_path
from django.views.static import serve


#def static(prefix, view=serve, **kwargs):
#    """
#    Return a URL pattern for serving files in debug mode.

#    from django.conf import settings
#    from django.conf.urls.static import static

#    urlpatterns = [
        # ... the rest of your URLconf goes here ...
#    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   """
#    if not prefix:
#        raise ImproperlyConfigured("Empty static prefix not permitted")
#    return [
#        re_path(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs),
#    ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('login.urls', namespace="login")),
    path('apply/', include('Application.urls', namespace="Application")),
    path('', include('Homepage.urls', namespace="Homepage")),
    path('department/', include('Department.urls', namespace="Department")),
    path('office/', include('Hostel_office.urls', namespace="Hostel_office")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
