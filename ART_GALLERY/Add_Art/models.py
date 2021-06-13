from django.db import models
from django.contrib.auth.models import User

class art(models.Model):
    artname=models.CharField(max_length=20,primary_key=True)
    category=models.CharField(max_length=20)
    prize=models.DecimalField(max_digits=1000, decimal_places=2)
    available=models.IntegerField(default=1)
    username=models.CharField(max_length=20,default='NOT SOLD')
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.artname + ": " + str(self.image)
