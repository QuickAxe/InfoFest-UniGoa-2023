from django.contrib.auth.models import AbstractUser
from django.db import models


# creating table for each user 
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    # Add custom fields here, if needed
  
    def __str__(self):
        return self.username