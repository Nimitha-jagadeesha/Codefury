from django.db import models
from django.utils import timezone
# Create your models here.
class Announcment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField() 

class Contact(models.Model):
    email= models.EmailField(blank = False)
    message= models.TextField()
    
