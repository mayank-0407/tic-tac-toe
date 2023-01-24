from django.db import models

# Create your models here.
class MediaFiles(models.Model):

    fname=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=30,null=True)
    photo=models.FileField(upload_to='media/',blank=True)
    
    def __str__(self):
        return self.fname