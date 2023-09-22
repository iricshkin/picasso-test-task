from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import settings
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("file.urls")),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
