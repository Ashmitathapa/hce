from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=120)
    phonenumber = models.IntegerField()
    username=models.CharField(max_length=70)

    def __str__(self):
        return self.name