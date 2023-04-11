from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views import generic
from django.contrib.auth.models import User

def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:10]
    return render(request,'posts/index.html', {'latest_post_list':latest_post_list})

@login_required
def submit_post(request):
    post_text = request.POST['new_post']
    user_posts = Post(post_text = post_text, user_name = request.user)
    user_posts.save()
    return HttpResponseRedirect(reverse('posts:index'))


def profile(request, user_name_id):
    selected_user = User.objects.get(pk=user_name_id)
    all_posts = Post.objects.filter(user_name = selected_user)
    return render(request,'posts/profile.html', {'all_posts':all_posts})
