from django.db import models

# Create your models here.

class Person(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    
class Automobile(models.Model):
    type=models.CharField(max_length=50)
    vname=models.CharField(max_length=40)
    cname=models.CharField(max_length=40)
    year=models.PositiveIntegerField()
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.vname + '  ' + self.cname
