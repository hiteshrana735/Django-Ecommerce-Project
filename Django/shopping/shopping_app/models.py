from django.db import models

# Create your models here.
class Cart(models.Model):
    product_name = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.product_name