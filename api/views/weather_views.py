from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token
from django.shortcuts import render

class Weather(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    def index(request):
      return render(request, 'weather/weather.html')
