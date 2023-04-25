from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    check_in_date = models.DateTimeField(default=timezone.now)
    check_out_date = models.DateTimeField(null=True)
    times_checked_out = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'

    def is_checked_out(self) -> bool:
        if self.check_out_date is None:
            return False
        return self.check_out_date > self.check_in_date
