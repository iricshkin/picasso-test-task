from rest_framework import serializers

from .models import File
from .tasks import process_file
from .validators import check_file_size


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(
        allow_empty_file=False, required=True, validators=[check_file_size]
    )

    class Meta:
        model = File
        fields = "__all__"
        read_only_fields = ("processed",)

    def create(self, validated_data):
        file = validated_data.pop("file")
        instance = File.objects.create(file=file, **validated_data)

        process_file.delay(instance.id)
        return instance
