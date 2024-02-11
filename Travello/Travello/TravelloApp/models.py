from django.db import models

# Create your models here.
class Nspot(models.Model):
    nspot_id=models.IntegerField(primary_key=True)
    nspot_name=models.CharField(max_length=50)
    type=(("india","india"),("international","innternational"))
    ncategory=models.CharField(max_length=100,choices=type)
    ndesc=models.CharField(max_length=255)
    nprice =models.IntegerField()
    nimage=models.ImageField(upload_to="pics")

class Ispot(models.Model):
    ispot_id=models.IntegerField(primary_key=True)
    ispot_name=models.CharField(max_length=50)
    type=(("india","india"),("international","innternational"))
    icategory=models.CharField(max_length=100,choices=type)
    idesc=models.CharField(max_length=255)
    iprice =models.IntegerField()
    iimage=models.ImageField(upload_to="pics")

class PassengerDetail(models.Model):
    pid=models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    date_created = models.DateTimeField()