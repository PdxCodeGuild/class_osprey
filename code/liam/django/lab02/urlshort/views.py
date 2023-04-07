from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import UrlShorten

from string import ascii_letters, digits
import random

def index(request):
    urls = UrlShorten.objects.all()
    template = loader.get_template('urlshort/index.html')
    context = { 
        'urls' : urls,
        }
    return HttpResponse(template.render(context, request))

def shorten(request, url_id):
    ...
    short_url = ''.join(random.choices(ascii_letters + digits, k=6))
    pass

def refer(request, url_id):
    ...
    # redirect of localhost/<str:shorturl>/ to full url assigned to it
    pass