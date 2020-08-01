from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('country-viewset/', views.CountryAPIView.as_view()),
    path('state-viewset/', views.StateAPIView.as_view()),
]