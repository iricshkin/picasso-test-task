from django.urls import path

from .views import UploadFileView


urlpatterns = [
    path("upload/", UploadFileView.as_view({"post": "create"}), name="upload"),
    path("files/", UploadFileView.as_view({"get": "list"}), name="list"),
]
