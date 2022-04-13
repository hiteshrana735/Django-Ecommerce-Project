from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=35)
    deptt = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name