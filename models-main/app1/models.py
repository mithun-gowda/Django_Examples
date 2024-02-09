from django.db import models

# Create your models here.

# class teacher(models.Model):
#     sid=models.CharField(max_length=20,primary_key=True)
#     studentname=models.CharField(max_length=30)
#     age=models.IntegerField()
#     contact_num=models.PositiveBigIntegerField()
#     email=models.EmailField(max_length=50)  #max_length for email field is not mandatory only for Charfield mandatory
#     location=models.CharField(max_length=30)
#     subject=models.CharField(max_length=40 ,default='abcd')
#     sal=models.PositiveIntegerField(null=True)
#     exp=models.PositiveIntegerField()

# class student1(models.Model):
#     sid=models.CharField(max_length=20,primary_key=True)
#     sname=models.CharField(max_length=50)
#     age=models.PositiveIntegerField()
#     number=models.PositiveBigIntegerField()
#     email=models.EmailField()


#     def __str__(self):
#         return self.sname
        

    #magic method which will get values as output in terminal (before it is showing)
    #<QuerySet [<student1: student1 object (s001)>]>  after using magic method

# ----------------------------------------------------------------------------------------------

class PersonalDetails(models.Model):
    pid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    mobile=models.PositiveBigIntegerField()
    email=models.EmailField()
    aadhar=models.PositiveBigIntegerField()
    age=models.PositiveIntegerField()

class School(models.Model):
    school_id=models.AutoField(primary_key=True)
    school_name=models.CharField(max_length=40)
    school_addr=models.CharField(max_length=50)
    principal=models.CharField(max_length=40)
    staff_no=models.PositiveIntegerField()


class Student(PersonalDetails,School):
    sid=models.CharField(max_length=20)
    standard=models.PositiveIntegerField()
    board=models.CharField(max_length=40)

class Teacher(PersonalDetails,School):
    tid=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    experience=models.PositiveIntegerField()
    sal=models.PositiveIntegerField()