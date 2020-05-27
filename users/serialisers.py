from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ("id", "email", "password", "first_name", "last_name")
        # fields = "__all__"
