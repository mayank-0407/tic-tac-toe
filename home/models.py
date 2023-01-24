from django.db import models
from django.contrib.auth.models import User
import datetime
from pytz import timezone
# Create your models here.

class Student(models.Model):
    
    fname=models.CharField(max_length=40,null=True)
    lname=models.CharField(max_length=40,null=True)
    age=models.IntegerField(default=1)
    gender= models.BooleanField(default=True)
    
    def __str__(self):

        return self.fname + " - " + self.flame