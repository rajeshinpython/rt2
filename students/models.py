from django.db import models

# Create your models here.
class StudentModel(models.Model):
    no = models.IntegerField(auto_created=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)


    
