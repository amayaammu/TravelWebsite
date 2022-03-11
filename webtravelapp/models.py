from django.db import models

# Create your models here.
class contactdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=False)
    phone=models.IntegerField(null=True,blank=False)
    message=models.CharField(max_length=100,null=True,blank=False)

class registerdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=False)
    phone=models.IntegerField(null=True,blank=False)
    uname=models.CharField(max_length=100,null=True,blank=False)
    password=models.CharField(max_length=100,null=True,blank=False)



