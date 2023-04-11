from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # automatically add the timestamp when the question is created
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    '''
    # automatically update the timestamp every time the question is saved
    pub_date = models.DateTimeField('date published', auto_now=True)
    # retain the ability to manually set the timestamp on creation if we want to
    pub_date = models.DateTimeField('date published', default=timezone.now)
    '''
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"'{self.choice_text}' for question: {self.question}"


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    vote_date = models.DateTimeField('date voted', default=timezone.now)

    def __str__(self) -> str:
        return f"{self.voter} voted for {self.choice}"
