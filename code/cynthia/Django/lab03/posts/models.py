from django.db import models

import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    post_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date posted', auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.post_text

