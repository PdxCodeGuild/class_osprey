from django.db import models

from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # automatically add the timestamp when the question is created
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    # automatically update the timestamp every time the question is saved
    pub_date = models.DateTimeField('date published', auto_now=True)

    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self) -> str:
        return f"{self.question_text}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"'{self.choice_text}' for question: {self.question}"
