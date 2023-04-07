from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.urls import reverse

from .models import UrlShorten, Click

from string import ascii_letters, digits
import random

def index(request):
    urls = UrlShorten.objects.order_by('-pk')[:1]
    template = loader.get_template('urlshort/index.html')
    context = { 
        'urls' : urls,
        }
    return HttpResponse(template.render(context, request))

def shorten(request):
    entry = request.POST['full-url-entry']
    long_url = entry
    entry = UrlShorten()
    entry.full_url = long_url
    entry.short_url = ''.join(random.choices(ascii_letters + digits, k=6))
    entry.save()
    return HttpResponseRedirect(reverse('urlshort:index'))

def refer(request, short_url):
    last_accessed_user = request.META['USERNAME']
    entry = get_object_or_404(UrlShorten, short_url=short_url)
    refer = entry.full_url
    entry.last_user = last_accessed_user
    entry.save()
    clicked = Click()
    clicked.url = entry
    clicked.accessed_by = last_accessed_user
    clicked.save()

    return HttpResponseRedirect(refer)