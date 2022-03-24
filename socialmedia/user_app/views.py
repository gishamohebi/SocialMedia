from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import *


class Home(View):
    def get(self, request):
        return render(request, 'user_app/home.html')


class DisplayPosts(ListView):
    """
    This will return the list of posts link to their details
    """
    model = Post


class PostDetail(DetailView):
    """
    This will return details of each post on a new tab
    """
    model = Post

    def get_context_data(self, *args, **kwargs):  # in order to show the comments and users of the comments
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        context["comments"] = Comment.objects.all().values()
        context["users"] = User.objects.all().values()
        return context


class NewPost(View):
    def get(self, request):
        form = PostModelForm()
        return render(request, 'user_app/new_post.html', {"form": form})

    def post(self, request):
        form = PostModelForm(request.POST, request.FILES)  # because of uploading images
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/user-app/display-posts/")
        else:
            return HttpResponse("No valid inputs")


def new_comment(request, post_id: int):
    if request.method == "GET":
        form = CommentModelForm()
        return render(request, 'user_app/new_comment.html', {"form": form})

    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = Comment(
                text=form.cleaned_data["text"],
                user=form.cleaned_data["user"],
                post=Post.objects.get(id=post_id)  # in order to set comment for the post
                # we selected,  we creat an object from comment model and use the id from url
            )
            comment.save()
            return HttpResponseRedirect(f"/user-app/postdetail/{post_id}")
        else:
            return HttpResponse("No valid inputs")


class PostsOfWeekList(View):
    def get(self, request):
        posts = Post.objects.posts_of_week()  # built the query with manager
        return render(request, "user_app/week_list.html", {"posts": posts})
