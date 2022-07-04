from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class student(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    firstname = models.CharField(max_length=25)
    secondname = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    course = models.CharField(max_length=25)
    batch = models.CharField(max_length=25)

    def __str__(self):
        return self.firstname

class course(models.Model):
    coursename = models.CharField(max_length=25)
    courseid = models.CharField(max_length=25)
    department = models.CharField(max_length=25)
    duration = models.CharField(max_length=25)
    fees = models.CharField(max_length=25)

    def __str__(self):
        return self.coursename

class staff(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)

    firstname = models.CharField(max_length=25)
    secondname = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    department = models.CharField(max_length=25)
    
    def __str__(self):
        return self.firstname

