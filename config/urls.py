from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("file.urls")),
]

if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)