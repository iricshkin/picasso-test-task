import factory
from django.test import TestCase
from file.models import File
import pytest
from unittest.mock import patch
from file.tasks import process_file
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from file.views import UploadFileView

from django.test import Client, TestCase
from file.models import File

class URLTest(TestCase):
    """Проверка доступности url."""

    def setUp(self):
        self.guest_client = Client()

    def test_upload_url_exists(self):
        response = self.guest_client.get("/upload/")
        self.assertEqual(response.status_code, 405)

    def test_files_url_exists(self):
        response = self.guest_client.get("/files/")
        self.assertEqual(response.status_code, 200)

class FileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = File

class TestFileModel(TestCase):
    """Проверка создания объекта модели File."""
    def test_create_file(self):
        file = FileFactory.create()
        self.assertEqual(File.objects.count(), 1)
        print(file.id)
        self.assertEqual(File.objects.first().id, file.id)


@pytest.mark.django_db
@patch("file.tasks.time.sleep", return_value=None)
@patch("file.tasks.File.objects.get")
def test_process_file(mock_get, mock_sleep):
    """Тесты для задач Celery."""

    file = "test_file.txt"
    mock_file = FileFactory.create(file=file)
    mock_get.return_value = mock_file
    process_file("mock_id")
    mock_file.refresh_from_db()
    assert mock_file.processed
    mock_sleep.assert_called_once()
