# models imports
from .models import Country,State,City,Town,Person

# serializers imports
from .serializers import CountrySerializer, StateSerializer, CitySerializer, TownSerializer, PersonSerializer

# rest_framework imports for view, Pagination , Filtering and Ordering
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CountryAPIView(APIView):

    def get(self, request, format=None):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class StateAPIView(APIView):

    def get(self, request, format=None):
        state = State.objects.all()
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)