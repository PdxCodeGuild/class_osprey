from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User
  
def index(request):
    posts = Post.objects.order_by("-post_date")
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)

def make_post(request):
    new_post = Post()
    new_post.content = request.POST['new_post']
    new_post.author = request.user
    new_post.save()
    print(request.user)
    return HttpResponseRedirect(reverse("posts:index"))

def profile_view(request, username):
    username = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=username)
    posts = posts.order_by("-post_date")
    context = {
        "posts": posts,
        "username" : username,
    }
    return render(request, "posts/profile.html", context)