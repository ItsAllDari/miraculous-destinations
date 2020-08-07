from django.db import models

from .user import User

# Create your models here.
class Location(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  country = models.CharField(max_length=3)
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The weather of '{self.city, self.state}' is {city_weather.temperature}"

  def as_dict(self):
    """Returns dictionary version of Location models"""
    return {
        'id': self.id,
        'city': self.city,
        'state': self.state,
        'country': self.country
    }
