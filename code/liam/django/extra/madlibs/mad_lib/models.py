from django.db import models
from django import forms

# Create your models here.
class MadLib(forms.Form):
    title = models.CharField('mad lib title', max_length=40)
    ...

    def __str__(self) -> str:
        return self.title

class MadLibWord(models.Model):
    word_for = models.ForeignKey(MadLib, on_delete=models.CASCADE)
