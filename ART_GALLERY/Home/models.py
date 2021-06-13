from django.db import models
from django.contrib.auth.models import User
from Add_Art.models import art

class view_cart(models.Model) :
    username=models.CharField(max_length=20)
    artname=models.CharField( max_length=20)
    models.ForeignKey(User, on_delete=models.CASCADE,default='maurya')
    models.ForeignKey(art, on_delete=models.CASCADE,default='artname')
    class Meta:
        unique_together = ('username','artname')
