from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import UrlShorten


def index(request):
    urls = UrlShorten.objects.all()
    template = loader.get_template('urlshort/index.html')
    context = { 
        'urls' : urls,
        }
    return HttpResponse(template.render(context, request))