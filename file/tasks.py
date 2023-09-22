import mimetypes
import time

from celery import shared_task

from .models import File
from config.settings import ANOTHER_MIME_TYPE_TIMEOUT, MIME_TYPE_TIMEOUTS


def get_mime_type_timeout(filename: str) -> int:
    """Метод определения таймаута для заданного типа MIME."""

    mimetype = mimetypes.guess_type(filename)[0].split("/")[0]
    return MIME_TYPE_TIMEOUTS.get(mimetype, ANOTHER_MIME_TYPE_TIMEOUT)


@shared_task
def process_file(file_id: str) -> None:
    """Функция обработки файла."""

    file = File.objects.get(id=file_id)
    timeout: int = get_mime_type_timeout(file.file.name)
    time.sleep(timeout)
    file.processed = True
    file.save()
