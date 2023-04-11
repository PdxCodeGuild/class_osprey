from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:10]
    return render(request,'posts/index.html', {'latest_post_list':latest_post_list})

@login_required
def submit_post(request):
    post_text = request.POST['new_post']
    user_posts = Post(post_text = post_text, user_name = request.user)
    user_posts.save()
    return HttpResponseRedirect(reverse('posts:index'))