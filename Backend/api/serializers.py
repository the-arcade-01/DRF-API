from rest_framework import serializers
from .models import Country, State, City, Town, Person

"""
    Person Serializer
"""
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name','country','state','city','town']
"""
    City Serializer
"""
class CitySerializer(serializers.ModelSerializer):
    person_city = PersonSerializer(many=True,read_only=True)
    class Meta:
        model = City
        fields = ['id','country','state','name','description','population','gdp','pin_code','person_city']
"""
    Town Serializer
"""
class TownSerializer(serializers.ModelSerializer):
    person_town = PersonSerializer(many=True,read_only=True)
    class Meta:
        model = Town
        fields = ['id','country','state','name','description','population','gdp','pin_code','person_town']
"""
    State Serializer
"""
class StateSerializer(serializers.ModelSerializer):
    city_state = CitySerializer(many=True,read_only=True)
    town_state = TownSerializer(many=True,read_only=True)
    class Meta:
        model = State
        fields = ['id','country','name','description','population','gdp','city_state','town_state']
"""
    Country Serializer
"""
class CountrySerializer(serializers.ModelSerializer):
    state_country = StateSerializer(many=True,read_only=True)
    class Meta:
        model = Country
        fields = ['id','name','description','population','gdp','state_country']
