from django.shortcuts import render
from .models import Country
from .serializers import CountrySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class CountryAPIView(APIView):
    
    def get(self,request):
        country = Country.objects.all()
        serializer = CountrySerializer(country,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class CountryAPIDetails(APIView):

    def get_object(self,id):
        try:
            return Country.objects.get(id = id)
        except Country.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self,request,id):
        country = self.get_object(id)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def put(self,request,id):
        country = self.get_object(id)
        serializer = CountrySerializer(country,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        country = self.get_object(id)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)