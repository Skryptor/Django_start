from django.db import models

from django.db import models


class Phone(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def __str__(self):
        return self.name

