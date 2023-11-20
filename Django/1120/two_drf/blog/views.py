from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 위 코드는 아래 코드와 같습니다.
# urls.py에서 url을 기본 제공하는 것만 사용해도 기본적으로 url도 분기해줍니다.
# def post_list(request):
#     # get
#     # post
#     pass

# def post_detail(request, pk):
#     # get
#     # put
#     # delete
#     pass



# 아래 코드는 저 기능중 단 1개만 사용합니다.
# class rest_framework import generics
# 
# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
# post_list = PostListAPIView.as_view()


# 위 코드는 아래 코드와 같습니다.
# def post_list(request):
#     # get