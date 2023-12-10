
from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=10, 
        error_messages={
            'max_length': '제목은 10자를 초과할 수 없습니닷!',
            'blank': '제목은 비워둘 수 없습니다.',
            'required': '제목은 필수 항목입니다.'
        }
    )
    content = serializers.CharField(
        max_length=100,
        error_messages={
            'max_length': '내용은 100자를 초과할 수 없습니닷!',
            'blank': '내용은 비워둘 수 없습니다.',
            'required': '내용은 필수 항목입니다.'
        }
    )