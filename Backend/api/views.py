from django.shortcuts import render
from .models import Country,State,City,Town
from .serializers import CountrySerializer, StateSerializer, CitySerializer, TownSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class TownViewSet(viewsets.ModelViewSet):
    serializer_class = TownSerializer
    queryset = Town.objects.all()
