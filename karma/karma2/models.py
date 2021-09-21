from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,)

    name_id = models.CharField(max_length=264,unique=True)


    mobile = models.IntegerField(unique=True)


    alternate_mobil_number= models.IntegerField(unique=True)


    address = models.CharField(max_length=100,unique=True)


    Address_line1 = models.CharField(max_length=100,unique=True)


    Address_line2 = models.CharField(max_length=100,unique=True)

    City = models.CharField(max_length=20,unique=True)

    State = models.CharField(max_length=20,unique=True)

    Zipcode = models.IntegerField(unique=True)

    Country = models.CharField(max_length=246,unique=True)



    def __str__(self):
        return self.name_id



