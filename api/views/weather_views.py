from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token
from django.shortcuts import render
import requests

class Weather(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    def index(request):
      url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=d5f16a9cc8b9f63fa4160694e460b64d'
      city = 'Boston'

      input = requests.get(url.format(city)).json()

      city_weather = {
          'city': city,
          'temperature': input['main']['temp'],
          'description': input['weather'][0]['description'],
          'icon': input['weather'][0]['icon']
      }
      # url = api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid=d5f16a9cc8b9f63fa4160694e460b64d
      print(city_weather)
      context = {'city_weather' : city_weather}
      return render(request, 'weather/weather.html')
