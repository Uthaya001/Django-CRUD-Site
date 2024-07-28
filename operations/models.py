from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=24)
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=250)
    jobrole=models.CharField(max_length=24)
    
    def __str__(self):
        return self.name
