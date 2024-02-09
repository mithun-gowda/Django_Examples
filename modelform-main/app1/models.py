from django.db import models

# Create your models here.

class TrainerModel(models.Model):
    empid=models.CharField(max_length=15,primary_key=True)
    name=models.CharField(max_length=30)
    experience=models.PositiveIntegerField()
    date_of_joining=models.DateField()
    salary=models.PositiveIntegerField()

    def __str__(self):
        return self.name  #for admin display else it will show object