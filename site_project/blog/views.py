from django.shortcuts import render
from django.http import Http404
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

def post_detail(request, id):
    """
    Представление детальной информации одиночного поста
    """
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist as post_not_found_exc:
        raise Http404("No Post found") from post_not_found_exc
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})