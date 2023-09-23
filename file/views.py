from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import GenericViewSet

from .error_message import error_responses
from .models import File
from .serializers import FileSerializer


@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Загрузка файла",
        responses={
            status.HTTP_400_BAD_REQUEST: error_responses[status.HTTP_400_BAD_REQUEST],
            status.HTTP_500_INTERNAL_SERVER_ERROR: error_responses[
                status.HTTP_500_INTERNAL_SERVER_ERROR
            ],
        },
    ),
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Получить список всех файлов",
        responses={
            status.HTTP_400_BAD_REQUEST: error_responses[status.HTTP_400_BAD_REQUEST],
            status.HTTP_404_NOT_FOUND: error_responses[status.HTTP_404_NOT_FOUND],
            status.HTTP_500_INTERNAL_SERVER_ERROR: error_responses[
                status.HTTP_500_INTERNAL_SERVER_ERROR
            ],
        },
    ),
)
class UploadFileView(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = File.objects.all().order_by("-id")
    serializer_class = FileSerializer
    http_method_names = ["get", "post"]

    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        operation_description="Загрузка файла",
        responses={
            status.HTTP_404_NOT_FOUND: error_responses[status.HTTP_404_NOT_FOUND],
            status.HTTP_500_INTERNAL_SERVER_ERROR: error_responses[status.HTTP_500_INTERNAL_SERVER_ERROR]
        })
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
