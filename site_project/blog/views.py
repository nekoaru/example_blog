from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
=======
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
>>>>>>> v.0.0.2
from .models import Post

# Create your views here.
def post_list(request):
    """
    Представление для всех опубликованных постов
    """
<<<<<<< HEAD
    posts = Post.published.all()
=======
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
>>>>>>> v.0.0.2
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

<<<<<<< HEAD
def post_detail(request, id):
=======
def post_detail(request, year, month, day, post):
>>>>>>> v.0.0.2
    """
    Представление детальной информации одиночного поста
    """
    post = get_object_or_404(Post,
<<<<<<< HEAD
                            id=id,
                            status=Post.Status.PUBLISHED)
=======
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,
                            slug=post,
                            status=Post.Status.PUBLISHED,)
>>>>>>> v.0.0.2
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
