from django.urls import path
from .views import daily_recommendation, home

urlpatterns = [
    path('', home, name='home'),  # Ana sayfa için URL
    path('api/recommendations/', daily_recommendation, name='daily_recommendation'),
]
