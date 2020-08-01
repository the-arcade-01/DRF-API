# models imports
from .models import Country,State,City,Town,Person

# serializers imports
from .serializers import CountrySerializer, StateSerializer, CitySerializer, TownSerializer, PersonSerializer

# rest_framework imports for view, Pagination , Filtering and Ordering
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter


# Country API viewset
class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

# State API viewset
class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

# City API viewset
class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

# Town API viewset
class TownViewSet(viewsets.ModelViewSet):
    serializer_class = TownSerializer
    queryset = Town.objects.all()

# Person API viewset
class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    # select_related for speeding up queries
    queryset = Person.objects.select_related('country','state','city','town')
    
    # pagination API created here
    pagination_class = PageNumberPagination

    # filtering based on Search and Ordering filter provided with below attributes
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('country__name','state__name','city__name','town__name','name')


