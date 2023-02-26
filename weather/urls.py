from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_weather_data, name='home'),
]