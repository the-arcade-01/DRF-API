from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

country_router = DefaultRouter()
country_router.register('api',views.CountryViewSet, basename='API')

state_router = DefaultRouter()
state_router.register('api',views.StateViewSet, basename='StateAPI')

urlpatterns = [
    path('country-viewset/',include(country_router.urls)),
    path('country-viewset/<int:id>/',include(country_router.urls)),
    path('state-viewset/',include(state_router.urls)),
    path('state-viewset/<int:id>/',include(state_router.urls)),
    # path('api/country',views.CountryAPIView.as_view()),
    # path('detail/country/<int:id>',views.CountryAPIDetails.as_view()),
]
