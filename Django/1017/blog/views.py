
# from django.shortcuts import render
# from .models import Post
# from datetime import date

# def postlist(request):
#     posts = Post.objects.all()
    
#     # 1. 연도와 일치되는 게시물 가져오기
#     # posts = Post.objects.filter(created_at__year=2023)
    
#     # 2. 월과 일치되는 게시물 가져오기
#     # posts = Post.objects.filter(created_at__month=10)

#     # 3. 일과 일치되는 게시물 가져오기
#     # posts = Post.objects.filter(created_at__day=16)

#     # 4. 연, 월, 일에 매칭이 되는 게시물 가져오기
#     # gt (greater than) : >
#     # lt (less than) : <
#     # gte (greater than or equal) : >=
#     # lte (less than or equal) : <=

#     # posts = Post.objects.filter(created_at__gte=date(2023,10,16))

#     # http://127.0.0.1:8000/blog/?q=hello
#     # 공식문서 : https://docs.djangoproject.com/en/4.2/ref/request-response/
#     return render(request, 'blog/postlist.html', {'posts':posts})

# from django.shortcuts import render
# from .models import Post
# from datetime import date

# def postlist(request):
#     posts = Post.objects.all()
#     # http://127.0.0.1:8000/blog/?q=hello
#     # 공식문서 : https://docs.djangoproject.com/en/4.2/ref/request-response/
#     print(request)
#     print(dir(request))
#     print(type(request))
#     # 여기에서 출력되는 것들은 templates에서도 출력 가능합니다.
#     # {{request.user}}
#     print(request.user)
#     print(type(request.user))
#     print(dir(request.user))
#     print(request.user.is_authenticated)
#     print(request.user.id) # user id는 1번
#     print(request.user.username)
#     print(request.user.is_superuser)
#     print(request.user.password)
#     print(request.GET)
#     print(request.GET.get('q'))
#     print(request.GET.get('q'))
#     print(dir(request.GET))
#     print(request.GET.get('hello', 'world')) # hello라는 쿼리가 없으면 world를 출력
#     print(request.POST)
#     print(request.FILES)
#     print(request.COOKIES) # Application > Cookies에 저장되어 있는 정보
#     print(request.path)
#     print(request.method)
#     print(request.get_full_path_info())
#     print(request.get_host())
#     return render(request, 'blog/postlist.html', {'posts':posts})

# # ###################################
# # 모델 실습 링크 : https://www.notion.so/paullabworkspace/Model-RDB-ERD-1-N-N-M-1-1-f34426c3b50c49c1adcda1a652dfa2c1

from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm

def postlist(request):
    posts = Post.objects.all()
    return render(request, 'blog/postlist.html', {'posts':posts})

def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment.objects.create(
                post=post,
                message=form.cleaned_data['message'],
                author=request.user
            )
        c.save()
    return render(request, 'blog/postdetail.html', {'post':post, 'form':form})

def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'blog/postlist.html', {'posts':posts})