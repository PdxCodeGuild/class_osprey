from django.db import models


class Conversion(models.Model):
    long_url = models.CharField(max_length=1000)
    short_code = models.CharField(max_length=1000)

    def __str__(self):
        return self.conversion_text
