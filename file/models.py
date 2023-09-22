from django.db import models


class File(models.Model):
    """Модель для файла."""

    file = models.FileField(upload_to="uploads/", max_length=256)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
