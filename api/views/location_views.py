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

from ..models.location import Location
from ..serializers import LocationSerializer, UserSerializer

class Locations(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
      """Index request"""
      # locations = Location.objects.all()
      locations = Location.objects.filter(owner=request.user.id)
      data = LocationSerializer(locations, many=True).data
      return Response(data)

    serializer_class = LocationSerializer

    def post(self, request):
      """Create request"""
      # Add user to request object
      request.data['location']['owner'] = request.user.id
      # Serialize/create location
      location = LocationSerializer(data=request.data['location'])
      if location.is_valid():
        l = location.save()
        return Response(location.data, status=status.HTTP_201_CREATED)
      else:
        return Response(locaton.errors, status=status.HTTP_400_BAD_REQUEST)

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
      return render(request, 'weather/weather.html', context)

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        location = get_object_or_404(Location, pk=pk)
        data = LocationSerializer(location).data
        # Only want to show owned locations?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this location')
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        location = get_object_or_404(Location, pk=pk)
        if not request.user.id == location.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this location')
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        if request.data['location'].get('owner', False):
            del request.data['location']['owner']

        # Locate Location
        location = get_object_or_404(Location, pk=pk)
        # Check if user is  the same
        if not request.user.id == location.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this location')

        # Add owner to data object now that we know this user owns the resource
        request.data['location']['owner'] = request.user.id
        # Validate updates with serializer
        ls = LocationSerializer(location, data=request.data['location'])
        if ls.is_valid():
            ls.save()
            print(ls)
            return Response(ls.data)
        return Response(ls.errors, status=status.HTTP_400_BAD_REQUEST)
