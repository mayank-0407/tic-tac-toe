from django.db import models
from django.contrib.auth.models import User
import datetime
# form pytz import timezone


# Create your models here.
class Tictac(models.Model):
    
    statuss=models.CharField(max_length=5,default="loss")
    winningIndex= models.CharField(max_length=4)
    IndexX= models.CharField(max_length=5)
    IndexO= models.CharField(max_length=5)
    
    def __str__(self):
        
        return self.statuss+"--"+self.winningIndex