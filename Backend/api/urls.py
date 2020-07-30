from django.urls import path, include
from . import views

urlpatterns = [
    path('api-country/',views.CountryAPIView.as_view()),
    path('detail-country/<int:id>',views.CountryAPIDetails.as_view()),
]
