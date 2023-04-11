from django.db import models

# from string import ascii_letters, digits
# import random

class UrlShorten(models.Model):
    full_url = models.CharField('full url', max_length=400)
    short_url = models.CharField('short url', max_length=6, default='TESTID')
    last_user = models.CharField('last user to redirect', max_length=30, default='nobody')

    def __str__(self) -> str:
        return self.short_url
    
class Click(models.Model):
    url = models.ForeignKey(UrlShorten, on_delete=models.CASCADE)
    accessed_by = models.CharField('accessed by', max_length=30, default='not_available')

    def __str__(self) -> str:
        return 'click data'