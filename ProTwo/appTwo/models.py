from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    
