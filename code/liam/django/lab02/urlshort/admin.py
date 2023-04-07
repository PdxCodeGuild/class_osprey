from django.contrib import admin
from .models import UrlShorten, Click

admin.site.register(UrlShorten)
admin.site.register(Click)