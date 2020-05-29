from django.db import models

# Create your models here.

class User(models.Model):
    studentId = models.TextField(blank=True)
    name = models.TextField(blank=True)
class history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    lab_name = models.TextField(blank=True)
    time = models.DateTimeField(blank=True)
