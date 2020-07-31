from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

country_router = DefaultRouter()
country_router.register('api',views.CountryViewSet, basename='API')

state_router = DefaultRouter()
state_router.register('api',views.StateViewSet, basename='StateAPI')

city_router = DefaultRouter()
city_router.register('api',views.CityViewSet, basename='CityAPI')

town_router = DefaultRouter()
town_router.register('api',views.TownViewSet, basename='TownAPI')

urlpatterns = [
    path('country-viewset/',include(country_router.urls)),
    path('country-viewset/<int:id>/',include(country_router.urls)),
    path('state-viewset/',include(state_router.urls)),
    path('state-viewset/<int:id>/',include(state_router.urls)),
    path('city-viewset/',include(city_router.urls)),
    path('city-viewset/<int:id>/',include(city_router.urls)),
    path('town-viewset/',include(town_router.urls)),
    path('town-viewset/<int:int>/',include(town_router.urls)),
    # path('api/country',views.CountryAPIView.as_view()),
    # path('detail/country/<int:id>',views.CountryAPIDetails.as_view()),
]
