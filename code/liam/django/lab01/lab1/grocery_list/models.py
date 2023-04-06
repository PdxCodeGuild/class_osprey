from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    text_description = models.CharField('grocery item', max_length=40)
    create_date = models.DateField('date added')
    complete_date = models.DateField('date completed', auto_now=True)
    complete = models.BooleanField(default=False)

    def __str__(self) :
        return self.text_description