from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    addrress = models.CharField(max_length=400)

    def __str__(self):
        return self.fullname