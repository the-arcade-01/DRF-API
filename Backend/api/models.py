from django.db import models

"""
    Country Model
    Attributes : name, description, population, gdp
    Ordering : gdp (ascending)
"""

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

"""
    State Model
    Attributes : country(Foreign Key to Country Model), name
                description, population, gdp
    Ordering : gdp (ascending)
"""

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

"""
    City Model
    Attributes : country(Foreign Key to Country Model), 
                state(Foreign Key to State Model),
                name, description, population, gdp, pin_code
    Ordering : gdp (ascending)
"""

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

"""
    Town Model
    Attributes : country(Foreign Key to Country Model), 
                state(Foreign Key to State Model),
                name, description, population, gdp, pin_code
    Ordering : gdp (ascending)
"""

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

"""
    Person Model
    Attributes : country(Foreign Key to Country Model), 
                state(Foreign Key to State Model),
                city(Foreign Key to City Model),
                town(Foreign Key to Town Model),
                name
    Ordering : gdp (ascending)
"""

class Person(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City,on_delete=models.SET_NULL,related_name='person_city',null=True)
    town = models.ForeignKey(Town,on_delete=models.SET_NULL,related_name='person_town',null=True)
    state = models.ForeignKey(State,on_delete=models.SET_NULL,related_name='person_state',null=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,related_name='person_country',null=True)

    def __str__(self):
        return f"Name {self.name}, Country {self.country}, City {self.city}, Town {self.town}, State {self.state}" 
