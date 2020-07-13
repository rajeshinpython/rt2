from django.db import models

# Create your models here.
class LogInModel(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)


class CourseModel(models.Model):
    name = models.CharField(max_length=30)
    faculty = models.CharField(max_length=30)
    date = models.DateField(help_text='YY-MM-DD')
    time = models.TimeField(help_text='24 Hours')
    fee = models.FloatField()
    duration = models.CharField(max_length=30)


    def __str__(self):
        return self.name