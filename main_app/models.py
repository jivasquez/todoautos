from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=200)

class City(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region)

class Brand(models.Model):
    name = models.CharField(max_length=200)
    
class Publication(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand)
    city = models.ForeignKey(City, null=True)
    region = models.ForeignKey(Region, null=True)
    publication_date = models.DateTimeField('date published')
    type_of_vehicle = models.CharField(max_length=200, blank=True)
    vehicle_body = models.CharField(max_length=200, blank=True)
    fuel = models.CharField(max_length=200, blank=True)
    at_transmission = models.NullBooleanField()
    air_conditioner = models.NullBooleanField()
    first_owner = models.NullBooleanField()
    centralized_locking = models.NullBooleanField()
    airbag = models.NullBooleanField()
    abs_break = models.NullBooleanField()
    kilometers = models.IntegerField(null=True)