from django.db import models

# Create your models here.
class Announcment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField() 
    