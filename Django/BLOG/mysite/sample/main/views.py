from django.shortcuts import render

def blog(request):
    # db = Cafe.objects.all()를 하면 아래와 같이 값을 가져오게 됩니다.
    db = {
        1: {
            'title': '제목 1', 
            'contents': 'Post 1 body', 
            'img': 'https://picsum.photos/200/300'
            },
        2: {
            'title': '제목 2', 
            'contents': 'Post 2 body', 
            'img': 'https://picsum.photos/200/300'
            },
        3: {
            'title': '제목 3', 
            'contents': 'Post 3 body', 
            'img': 'https://picsum.photos/200/300'
            },
    }
    return render(request, 'blog/blog.html')

def post(request, pk):
    # db = Cafe.objects.get(pk=pk)
    return render(request, 'blog/post.html')

def bookinfo(request):
    '''
    교육용 크롤링 페이지입니다.
    '''
    return render(request, 'blog/bookinfo.html')