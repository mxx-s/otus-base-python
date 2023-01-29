from django.shortcuts import render

from posts.models import Post

# Create your views here.

def main_page(request):
    posts=Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, "posts/index.html", context=context)
