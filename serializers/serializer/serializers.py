import datetime
import re

from rest_framework import serializers
from .models import Comment


class CommentSerializerWithOutCustomValidate(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.content = validated_data.get("content", instance.content)
        instance.created = validated_data.get("created", instance.created)
        instance.save()
        return instance


class CommentSerializerWithFieldValidate(serializers.Serializer):
    email = serializers.CharField()
    content = serializers.CharField(max_length=10)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.content = validated_data.get("content", instance.content)
        instance.created = validated_data.get("created", instance.created)
        instance.save()
        return instance

    # validate 함수들
    # validate_<필드명> 작성시 자동으로 사용된다.

    def validate_email(self, email):
        EMAIL_REGEX = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if not re.fullmatch(EMAIL_REGEX, email):
            raise serializers.ValidationError("Invalid Email")

        return email

    def validate_content(self, content):
        if type(content) != str:
            raise serializers.ValidationError
        return content

    def validate_created(self, created):
        if type(created) != datetime.datetime:
            raise serializers.ValidationError

        return created


class CommentSerializerWithObjectValidate(serializers.Serializer):
    email = serializers.CharField()
    content = serializers.CharField(max_length=10)
    created = serializers.DateTimeField()

    def validate(self, data):
        EMAIL_REGEX = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        email = data["email"]
        content = data["email"]
        created = data["created"]

        if not re.fullmatch(EMAIL_REGEX, email):
            raise serializers.ValidationError("Invalid Email")

        if type(content) != str:
            raise serializers.ValidationError

        if type(created) != datetime.datetime:
            raise serializers.ValidationError

        return data
