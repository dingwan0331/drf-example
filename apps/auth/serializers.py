from rest_framework import serializers

from apps.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username"]
        extra_kwargs = {"password": {"write_only": True}}
