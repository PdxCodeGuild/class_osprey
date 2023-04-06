from django.db import models
from string import ascii_letters, digits
import random

class UrlShorten(models.Model):
    full_url = models.CharField('full url', max_length=400)
    short_url = ''.join(random.choices(ascii_letters + digits, k=6))

    def __str__(self) -> str:
        return self.short_url