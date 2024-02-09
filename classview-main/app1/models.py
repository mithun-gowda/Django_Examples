from django.db import models

# Create your models here.

class Cart(models.Model):
    pid=models.CharField(max_length=10,primary_key=True)
    product=models.CharField(max_length=30)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return self.product