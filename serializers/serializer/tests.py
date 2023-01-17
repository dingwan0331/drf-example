from datetime import datetime

from .models import Comment
from .serializers import (
    CommentSerializerWithOutCustomValidate,
    CommentSerializerWithFieldValidate,
)

INVALID_DATA = {"a": 1, "b": 2, "c": 3}
VALID_DATA = {"email": "lak@na.com", "content": "a", "created": datetime.now()}


def call_create_with_save(data):
    print("call_create_with_save")
    try:
        # 키워드 인자로 data 하나만 넣었기때문에 save시 create메서드를 호출한다.
        comment = CommentSerializerWithOutCustomValidate(data=data)
        print("is_valid: ", comment.is_valid())
        print("comment_errors: ", comment.errors)
        print("comment.validated_data: ", comment.validated_data)
        # comment의  is_valid를 통과 못할 시 raise
        print("comment instance: ", comment.save())

    except Exception as e:
        print(e)


def call_update_with_save(data):
    print("call_update_with_save")
    try:
        # save시 DB object와 data두가지를 인자로 넣었기에 update메서드를 호출한다.
        comment_raw = Comment.objects.last()
        comment = CommentSerializerWithOutCustomValidate(comment_raw, data=data)
        print("is_valid: ", comment.is_valid())
        print("comment_errors: ", comment.errors)
        print("comment.validated_data: ", comment.validated_data)
        # comment의  is_valid를 통과 못할 시 raise
        print("comment instance: ", comment.save())

    except Exception as e:
        print(e)


def call_save_with_raise_exception(data):
    print("call_save_with_raise_exception")
    try:
        # save시 DB object와 data두가지를 인자로 넣었기에 update메서드를 호출한다.
        comment_raw = Comment.objects.last()
        comment = CommentSerializerWithOutCustomValidate(comment_raw, data=data)
        # comment의  is_valid를 통과 못할 시 raise
        print("is_valid: ", comment.is_valid(raise_exception=True))
        print("comment_errors: ", comment.errors)
        print("comment.validated_data: ", comment.validated_data)
        print("comment instance: ", comment.save())

    except Exception as e:
        print(e)


def call_field_level_validate(data):
    print("call_field_level_validate")
    try:
        comment = CommentSerializerWithFieldValidate(data=data)

        print("is_valid: ", comment.is_valid())
        print("comment_errors: ", comment.errors)
        print("comment.validated_data: ", comment.validated_data)
        print("comment instance: ", comment.save())

    except Exception as e:
        print(e)
