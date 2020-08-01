from rest_framework import serializers, status
from .models import Country, State, City, Town, Person
from rest_framework.response import Response

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name','country','state','city','town']

class CitySerializer(serializers.ModelSerializer):
    person_town = serializers.SerializerMethodField('related_person')
    class Meta:
        model = Town
        fields = ['id','country','state','name','description','population','gdp','pin_code','person_city']

    def create(self, validated_data):
        return City.objects.create(**validated_data)

    def update(self, instance, validated_data):
        try:
            instance.state = validated_data.get('state', instance.state)
            instance.country = validated_data.get('country', instance.country)
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.population = validated_data.get('population', instance.population)
            instance.gdp = validated_data.get('gdp', instance.gdp)
            instance.pin_code = validated_data.get('pin_code', instance.pin_code)
            instance.save()
        except City.DoesNotExist:
             return Response(status=status.HTTP_204_NO_CONTENT)
    

    def related_person(self,validated_data):
        person_obj = PersonSerializer(Person.objects.filter(city__name=validated_data.name), many=True)
        return person_obj.data

class TownSerializer(serializers.ModelSerializer):
    person_town = serializers.SerializerMethodField('related_person')
    class Meta:
        model = Town
        fields = ['id','country','state','name','description','population','gdp','pin_code','person_town']

    def create(self, validated_data):
        return Town.objects.create(**validated_data)

    def update(self, instance, validated_data):
        try:
            instance.state = validated_data.get('state', instance.state)
            instance.country = validated_data.get('country', instance.country)
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.population = validated_data.get('population', instance.population)
            instance.gdp = validated_data.get('gdp', instance.gdp)
            instance.pin_code = validated_data.get('pin_code', instance.pin_code)
            instance.save()
        except Town.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def related_person(self,validated_data):
        person_obj = PersonSerializer(Person.objects.filter(town__name=validated_data.name), many=True)
        return person_obj.data


class StateSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField('related_city')
    town = serializers.SerializerMethodField('related_town')
    
    class Meta:
        model = Country
        fields = ['id','country','name','description','population','gdp','city','town']

    def update(self, instance, validated_data):
        try:
            instance.country = validated_data.get('country', instance.country)
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.population = validated_data.get('population', instance.population)
            instance.gdp = validated_data.get('gdp', instance.gdp)
            instance.save()
        except State.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, validated_data):
        return State.objects.create(**validated_data)

    def related_city(self, validated_data):
        city_obj = CitySerializer(City.objects.filter(state__name=validated_data.name), many=True)
        return city_obj.data

    def related_town(self, validated_data):
        town_obj = TownSerializer(Town.objects.filter(state__name=validated_data.name), many=True)
        return town_obj.data

class CountrySerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField('related_state')

    class Meta:
        model = Country
        fields = ['id','name','description','population','gdp','states']
    
    def create(self, validated_data):
        return Country.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.population = validated_data.get('population', instance.population)
        instance.gdp = validated_data.get('gdp', instance.gdp)
        instance.save()

    def related_state(self, validated_data):
        state_obj =  StateSerializer(State.objects.filter(country__name=validated_data.name), many=True)
        return state_obj.data