# -*- encoding: utf-8 -*-

from django.db import models
from elasticsearch_dsl import DocType, String


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=200)

class City(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region)

class Brand(models.Model):
    name = models.CharField(max_length=200)
    
class Publication_index(DocType):
    title = String(analyzer='snowball')
    brand = String(analyzer='snowball')
    class Meta:
        index = 'publications'

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
    confirmed = models.BooleanField(default=False)


    

    CHARACTERISTICS = [
      { 'key': 'brand', 'label': 'Marca', 'type': 'brand'},
      { 'key': 'type_of_vehicle', 'label': 'Tipo de vehículo', 'type': 'string'},
      { 'key': 'vehicle_body', 'label': 'Chasis', 'type': 'string'},
      { 'key': 'fuel', 'label': 'Tipo de combustible', 'type': 'string'},
      { 'key': 'at_transmission', 'label': 'Transmisión', 'type': 'custom_boolean', 'alternatives': {'True': 'Automática', 'False': 'Mecánica'}},
      { 'key': 'air_conditioner', 'label': 'Aire acondicionado', 'type': 'boolean'},
      { 'key': 'first_owner', 'label': 'Primer dueño', 'type': 'boolean'},
      { 'key': 'centralized_locking', 'label': 'Cierre centralizado', 'type': 'boolean'},
      { 'key': 'airbag', 'label': 'Airbag', 'type': 'boolean'},
      { 'key': 'abs_break', 'label': 'Frenos ABS', 'type': 'boolean'},
      { 'key': 'kilometers', 'label': 'Kilómetros', 'type': 'integer'}
    ]

    
    def get_characteristics(self):

      for characteristic in self.CHARACTERISTICS:
        if characteristic.get('type') == 'boolean':
          characteristic['value'] = "Si" if self.__dict__[characteristic.get('key')] else "No"
        if characteristic.get('type') == 'string':
          characteristic['value'] = self.__dict__[characteristic.get('key')]
        if characteristic.get('type') == 'custom_boolean':
          characteristic['value'] = characteristic.get('alternatives').get('True') if self.__dict__[characteristic.get('key')] else characteristic.get('alternatives').get('False')
        if characteristic.get('type') == 'integer':
          characteristic['value'] = self.__dict__[characteristic.get('key')]
        if characteristic.get('type') == 'brand':
          characteristic['value'] = self.brand.name
      return self.CHARACTERISTICS