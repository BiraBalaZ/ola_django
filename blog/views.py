from blog.data import posts
from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        'text': 'Olá Blog',
        'title': 'Blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
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
