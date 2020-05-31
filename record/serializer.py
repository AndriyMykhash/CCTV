from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    time = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Record(**validated_data)

    class Meta:
        model = Record
        fields = "__all__"
