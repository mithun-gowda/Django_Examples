from django.db import models

# Create your models here.

class Product(models.Model):
    pid=models.AutoField(primary_key=True )
    pname=models.CharField(max_length=30)
    brand=models.CharField(max_length=40)
    price=models.PositiveIntegerField()


class Details(models.Model):
    name=models.CharField(max_length=30)
    mob=models.PositiveBigIntegerField()
    email=models.EmailField()
    addr=models.CharField(max_length=100)

    class Meta:
        abstract = True    #abstract class

class Student(Details):
    sid=models.CharField(max_length=30,primary_key=True)
    std=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()

class Stu(Student):
    class Meta:
        proxy = True      #proxy class

class Teacher(Details):
    tid=models.CharField(max_length=30,primary_key=True)
    subject=models.CharField(max_length=30)
    sal=models.PositiveIntegerField()