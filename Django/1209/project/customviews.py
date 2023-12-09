# customviews.py
from django.http import HttpResponse
from django.http import JsonResponse
import json
from rest_framework import serializers
from rest_framework.response import Response

# # 1
# def index(request):
#     return HttpResponse("Hello, world.")

# # 2
# def index(request):
#     data = {
#         "name": "Django",
#         "age": 15,
#     }
#     return HttpResponse(data)

# # 3
# def index(request):
#     data = {
#         "name": "Django",
#         "age": 15,
#     }
#     return HttpResponse(str(data))

# # 4
# def index(request):
#     function = {
#         "add": add,
#         "sub": "빼기",
#     }
#     data = {
#         "name": "Django",
#         "age": 15,
#         "function": function
#     }
#     return HttpResponse(str(data))


# 4
# def index(request):
#     function = {
#         "add": add,
#         "sub": "빼기",
#     }
#     data = {
#         "name": "Django",
#         "age": 15,
#         "function": function
#     }
#     return HttpResponse(str(data))


# 6
def index(request):
    function = {
        "add": "더하기",
        "sub": "빼기",
    }
    data = {"name": "Django", "age": 15, "function": function}
    # return HttpResponse("<h1>This is HTML</h1>", content_type="text/html")
    # return HttpResponse(str(data), content_type="application/json")
    return JsonResponse(data)


# 7
# def index(request):
#     data = [1, 2, 3, 4]
#     return HttpResponse(json.dumps(data))


# # 8
# def index(request):
#     data = [1, 2, 3, 4]
#     return HttpResponse(data)


# # 9
# # 실제 해결하려는 문제는 더 복잡할 수 있습니다.
# # 실습 X
# class PostSerializer(serializers.Serializer):
#     pass


# def index(request):
#     author = [
#         {"id": 1, "name": "Django 1"},
#         {"id": 2, "name": "Django 2"},
#         {"id": 3, "name": "Django 3"},
#     ]
#     s1 = {
#         "author": 1,
#         "content": "hello 1",
#     }
#     s2 = {
#         "author": 2,
#         "content": "hello 2",
#     }
#     s3 = {
#         "author": 3,
#         "content": "hello 3",
#     }
#     posts = [
#         {"title": "1", "content": s1},
#         {"title": "2", "content": s2},
#         {"title": "3", "content": s3},
#     ]
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)