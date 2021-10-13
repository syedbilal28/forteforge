from django.db import models
from django.contrib.auth.models import User
from cities_light.models import City,Country
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField()
    postal_code = models.IntegerField()
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    portfolio = models.FileField()


class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()   
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    company=models.CharField(max_length=100,null=True)
    message=models.CharField(max_length=1000,null=True)

class EnterPriseContact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()


