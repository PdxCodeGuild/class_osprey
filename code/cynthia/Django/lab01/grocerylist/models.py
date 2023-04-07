from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    item_description = models.CharField(max_length=100)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    purchased_item = models.BooleanField()
    if purchased_item ==True:
        completed_date = models.DateTimeField('completed date', default=timezone.now)
    
    def __str__(self):
        return self.item_description 