from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname=models.CharField(max_length=100)
    relationship=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=300)

    def __str__(self):
        return self.fullname

    
