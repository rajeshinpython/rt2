from django.db import models
from Admin1.models import CourseModel

# Create your models here.
class StudentModel(models.Model):
    no = models.IntegerField(auto_created=True,null=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    enrol = models.ManyToManyField(CourseModel,blank=True)


    def __str__(self):
        return self.name
    
