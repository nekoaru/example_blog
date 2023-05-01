from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.
def post_list(request):
    """
    Представление для всех опубликованных постов
    """
    NUM_POSTS = 5
    
    post_list = Post.published.all()
    paginator = Paginator(post_list, NUM_POSTS)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # При обращении к странице с не целым числом - выдача первой страницы
        posts = paginator.page(1)
    except EmptyPage:
        # При обращении вне диапозона - выдача последней страницы
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, year, month, day, post):
    """
    Представление детальной информации одиночного поста
    """
    post = get_object_or_404(Post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,
                            slug=post,
                            status=Post.Status.PUBLISHED,)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
