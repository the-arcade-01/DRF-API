from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    population = models.IntegerField()
    gdp = models.FloatField()

    class Meta:
        unique_together = ['name']
        ordering = ['gdp']

    def __str__(self):
        return "Country: "+self.name

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='state_country')
    name = models.CharField(max_length=100)
    description = models.TextField()
    population = models.IntegerField()
    gdp = models.FloatField()

    class Meta:
        unique_together = ['country','name']
        ordering = ['gdp']

    def __str__(self):
        return "State: "+self.name

class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='city_country')
    state = models.ForeignKey(State,on_delete=models.CASCADE,related_name='city_state')
    name = models.CharField(max_length=100)
    description = models.TextField()
    population = models.IntegerField()
    gdp = models.FloatField()
    pin_code = models.CharField(max_length=10)

    class Meta:
        unique_together = ['country','state','name','pin_code']
        ordering = ['gdp']

    def __str__(self):
        return "City: "+self.name

class Town(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name="town_country")
    state = models.ForeignKey(State,on_delete=models.CASCADE,related_name='town_state')
    name = models.CharField(max_length=100)
    description = models.TextField()
    population = models.IntegerField()
    gdp = models.FloatField()
    pin_code = models.CharField(max_length=10)

    class Meta:
        unique_together = ['country','state','name','pin_code']
        ordering = ['gdp']

    def __str__(self):
        return "Town: "+self.name

 