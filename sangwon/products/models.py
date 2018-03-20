from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=10)
    description = models.TextField(
        max_length=150,
    )

    def __str__(self):
        return self.name
