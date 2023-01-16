from datetime import datetime

from .models import Comment
from .serializers import CommentSerializer

invalid_data = {"a": 1, "b": 2, "c": 3}
valid_data = {"email": "lak@na.com", "content": "a", "created": datetime.now()}


def call_save_with_invalid_data(data):
    try:
        # 키워드 인자로 data 하나만 넣었기때문에 save시 create메서드를 호출한다.
        comment = CommentSerializer(data=invalid_data)
        print("is_valid: ", comment.is_valid())
        print("comment_errors: ", comment.errors)
        print("comment.validated_data: ", comment.validated_data)
        # comment의  validated_data를 인자로 create메서드를 호출한다.
        # 빈 dict이기 때문에 이경우 raise발생
        comment.save()

    except Exception as e:
        print(e)


def call_save_with_valid_data(data):
    try:
        # 키워드 인자로 data 하나만 넣었기때문에 save시 create메서드를 호출한다.
        comment = CommentSerializer(data=valid_data)
        print("is_valid: ", comment.is_valid())
        print("comment_errors: ", comment.errors)
        print("comment.validated_data: ", comment.validated_data)
        # comment의  validated_data를 인자로 create메서드를 호출한다.
        comment.save()

    except Exception as e:
        print(e)
