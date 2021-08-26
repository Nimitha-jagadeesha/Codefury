from django.db import models

# Create your models here.
class Announcment(models.Model):
    title = models.CharField(max_length=300, blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField(blank = False)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.email
    
class Question(models.Model):
    question = models.TextField(max_length = 100)
    answer = models.TextField(max_length = 400)

    def __str__(self):
        return self.question