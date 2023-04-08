from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Conversion

import random
import string

letter = string.ascii_letters
punctuation = string.punctuation  
digits = string.digits 
choices = letter + punctuation + digits 


def index(request):
    url_database = Conversion.objects.all()
    context = {'url_database':url_database}
    return render(request, 'shortener/index.html', context)

#submit a url
def submit_url(request):
    short_code = 'shorturl.'
    while len(short_code) < 18:
        short_code += random.choice(choices) 
    long_url = request.POST['long_url']
    user_submission = Conversion(long_url = long_url, short_code = short_code)
    user_submission.save()
    return HttpResponseRedirect(reverse('shortener:index'))


