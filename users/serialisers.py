from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User(**validated_data)

    class Meta:
        model = User
        fields = ("id", "email", "password", "first_name", "last_name")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def get_token(self, user):
        token = super(MyTokenObtainPairSerializer, self).get_token(user)
        token['email'] = user.email
        return token
