from rest_framework import serializers
from .models import Country, State, City, Town

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','country','state','name','description','population','gdp']

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ['id','country','state','name','description','population','gdp']

class StateSerializer(serializers.ModelSerializer):
    city_state = CitySerializer(many=True,read_only=True)
    town_state = TownSerializer(many=True,read_only=True)
    class Meta:
        model = State
        fields = ['id','country','name','description','population','gdp','city_state','town_state']

class CountrySerializer(serializers.ModelSerializer):
    state_country = StateSerializer(many=True,read_only=True)
    class Meta:
        model = Country
        fields = ['id','name','description','population','gdp','state_country']

    # def create(self, validated_data):
    #     state_data = validated_data.pop('state_country')
    #     country_data = Country.objects.create(**validated_data)
    #     for item in state_data:
    #         State.objects.create(country=country_data, **item)
    #     return country_data

    # def update(self, instance, validated_data):
    #     state_data = validated_data.pop('state_country')
    #     state = (instance.state_country).all()
    #     state = list(state)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.population = validated_data.get('population', instance.population)
    #     instance.population = validated_data.get('gdp', instance.gdp)
    #     instance.save()

    #     for item in state_data:
    #         state_obj = state.pop(0)
    #         state_obj.name = item.get('name', state_obj.name)
    #         state_obj.description = item.get('description', state_obj.description)
    #         state_obj.population = item.get('population', state_obj.population)
    #         state_obj.gdp = item.get('gdp',state_obj.gdp)
    #         state_obj.save()
    #     return instance