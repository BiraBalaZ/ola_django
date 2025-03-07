from typing import Any

from blog.data import posts
from django.http import Http404, HttpRequest
from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        'title': 'Blog',
        'posts': posts,
    }

    return render(
        request,
        'blog/index.html',
        context,
    )

def post(request:HttpRequest, post_id: int):
    print('post', post_id)

    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        # 'title': f'Post {post_id}',
        'post': found_post,
        'title': found_post ['title'],
    }

    return render(
        request,
        'blog/post.html',
        context,
    )

def exemplo(request):
    print('exemplo')

    contexto = {
        'text': 'Olá Exemplo',
        'title': 'Exemplo',
    }

    return render(
        request,
        'blog/exemplo.html',
        contexto,
    )
