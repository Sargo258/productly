from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    score = models.FloatField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    created_in = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
