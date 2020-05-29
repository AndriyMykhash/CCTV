from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    time = serializers.ReadOnlyField()

    # id = serializers.IntegerField()
    def create(self, validated_data):
        return Record(**validated_data)

    class Meta:
        model = Record
        fields = "__all__"
        # fields = ['name', "time", 'image']
