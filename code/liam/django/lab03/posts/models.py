from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post_date = models.DateTimeField("posted date", auto_now=True)
    content = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.content