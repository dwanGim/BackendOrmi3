# blog > serializers.py
from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    '''
    아래 max_length와 같은 값은 유효성 검사를 위한 제약조건입니다.
    데이터가 11자여도 애러이고, 들어온 데이터가 11자여도 애러입니다.
    '''
    title = serializers.CharField(max_length=10)
    content = serializers.CharField(max_length=100)