from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from posts.models import Post
from .forms import PostModelForm

# Create your views here.


def main_page(request):
    posts = Post.objects.all().values(
        "id",
        "title",
        "body",
        "autor__name",
        "comment__id",
        "comment__body",
        "comment__author__name",
    )

    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)


# CRUD - Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    # fields = ('title', 'body', 'autor')
    form_class = PostModelForm
    success_url = reverse_lazy("posts")


class PostUpdateView(UpdateView):
    model = Post
    # fields = ('title', 'body', 'autor')
    form_class = PostModelForm
    success_url = reverse_lazy("posts")


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("posts")
