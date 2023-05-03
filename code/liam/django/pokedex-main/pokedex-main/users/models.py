from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # caught = the set of Pokemon associated with that user
    caught = []

    # This is where you would add additional fields.
    # These will be in the DB alongside username, email, etc

    def __str__(self):
        return self.username
