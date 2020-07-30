from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100,unique=True,)
    description = models.TextField()
    population = models.IntegerField()
    gdp = models.FloatField()

    def __str__(self):
        return self.name