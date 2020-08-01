from django.urls import path, include
from . import views

# for mapping default route 'api' to all class of views
from rest_framework.routers import DefaultRouter

# for country
country_router = DefaultRouter()
country_router.register('api',views.CountryViewSet, basename='API')

# for state
state_router = DefaultRouter()
state_router.register('api',views.StateViewSet, basename='StateAPI')

# for city
city_router = DefaultRouter()
city_router.register('api',views.CityViewSet, basename='CityAPI')

# for town
town_router = DefaultRouter()
town_router.register('api',views.TownViewSet, basename='TownAPI')

# for person
person_router = DefaultRouter()
person_router.register('api',views.PersonViewSet, basename='PersonAPI')

urlpatterns = [
    # Country API
    path('country-viewset/',include(country_router.urls)),
    path('country-viewset/<int:id>/',include(country_router.urls)),
    
    # State API
    path('state-viewset/',include(state_router.urls)),
    path('state-viewset/<int:id>/',include(state_router.urls)),
    
    # City API
    path('city-viewset/',include(city_router.urls)),
    path('city-viewset/<int:id>/',include(city_router.urls)),
    
    # Town API
    path('town-viewset/',include(town_router.urls)),
    path('town-viewset/<int:id>/',include(town_router.urls)),
    
    # Person API
    path('person-viewset/',include(person_router.urls)),
    path('person-viewset/<int:id>/',include(person_router.urls)),
]
