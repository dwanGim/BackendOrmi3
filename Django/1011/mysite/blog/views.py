from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

def blog(request):
    return render(request, 'blog/blog.html')

def post(request, pk):
    return render(request, 'blog/post.html')

def test(request, pk):
    data = [
        {'title': 'Post 1', 'text': 'Text 1', 'pk': 1},
        {'title': 'Post 2', 'text': 'Text 2', 'pk': 2},
        {'title': 'Post 3', 'text': 'Text 3', 'pk': 3},
    ]
    # return render(request, 'blog/post.html')
    return HttpResponse('Hello World')