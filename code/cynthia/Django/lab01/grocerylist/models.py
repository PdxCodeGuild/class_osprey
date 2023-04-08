from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    item_description = models.CharField(max_length=100)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField('completed date', null = True)

    def __str__(self):
        return self.item_description 