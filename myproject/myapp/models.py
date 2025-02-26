from django.db import models

# Create your models here.

class MyTable(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=80)
    email=models.CharField(max_length=80)
    password=models.CharField(max_length=80)

class PersonalDetails(models.Model):
    regid=models.ForeignKey(MyTable,on_delete=models.CASCADE)
    name=models.CharField(max_length=80)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=80)

class gallery(models.Model):
    regid = models.ForeignKey(MyTable,on_delete=models.CASCADE)
    photo = models.FileField(upload_to='media')
   