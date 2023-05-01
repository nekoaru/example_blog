from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    """
    Представление для всех опубликованных постов
    """
    posts = Post.published.all()
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
