from django.db import models

# Create your models here.
class traveldb(models.Model):
    destination=models.CharField(max_length=100,null=True,blank=False)
    location=models.CharField(max_length=100,null=True,blank=False)
    price=models.IntegerField(null=True,blank=False)
    image=models.ImageField(upload_to='image',null=True,blank=False)