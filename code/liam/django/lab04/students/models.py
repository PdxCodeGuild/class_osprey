from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField('first name',max_length=20)
    last_name = models.CharField('last name',max_length=25)
    cohort = models.CharField('cohort',max_length=25)
    favorite_topic = models.CharField('favorite topic',max_length=200)
    favorite_teacher = models.CharField('favorite teacher', max_length=20)
    capstone = models.URLField('capstone project')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'