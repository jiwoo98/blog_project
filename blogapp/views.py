from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all() #블로그 모든 글을 대상으로
    paginator = Paginator(blog_list, 3) # 블로그 객체 세 개를 한 페이지로 자르기
    page = request.GET.get('page') # request된 페이지가 뭔 지를 알아내고 
    posts = paginator.get_page(page) #request된 페이지를 얻어온 뒤
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def blogpost(request):
    #입력된 내용을 처리하는 기능 = POST
    #빈 페이지를 띄워주는 기능 = GET
    if request.method == 'POST' :
        form = blogPost(request.POST)
        if form.is_valid(): #형식에 맞게 입력됐다면
            post = form.save(commit=False) #모델 객체를 반환하되, 아직은 저장하지 않는다
            post.pub_date = timezone.now() #입력공간에 적어주지 않은 곳에
            post.save()
            return redirect('home')
    else :
        form = BlogPost()
        return render(request, 'new.html', {'form':form})