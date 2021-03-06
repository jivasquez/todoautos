# -*- encoding: utf-8 -*-
import re

import requests
from django.db import models
from django.conf import settings
from elasticsearch_dsl import DocType, String, Integer, Float, Date, Boolean
from elasticsearch_dsl.connections import connections
from sorl.thumbnail import ImageField, get_thumbnail
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from celery import Celery

from todoautosscraper.chileautos_scraper import ChileautosScrapper

app = Celery('models', backend='rpc://', broker='amqp://guest@localhost//')
connections.create_connection(hosts=['localhost'])

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=200)

class City(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, null=True)

class Brand(models.Model):
    name = models.CharField(max_length=200)

class Publication_index(DocType):
    title = String(analyzer='snowball')
    description = String(analyzer='snowball')
    price = Integer()
    source = String(analyzer='snowball')
    chileautos_id = Integer()
    brand = String(analyzer='snowball')
    model = String(analyzer='snowball')
    model_version = String(analyzer='snowball')
    plate_number = String(analizer='snowball')
    city = String(analyzer='snowball')
    region = String(analyzer='snowball')
    year = Integer()
    # publication_date = Date()
    type_of_vehicle = String(analyzer='snowball')
    vehicle_body = String(analyzer='snowball')
    color = String(analyzer='snowball')
    fuel = String(analyzer='snowball')
    engine = Float()
    doors = Integer()
    at_transmission = Boolean()
    assisted_steering = Boolean()
    air_conditioner = Boolean()
    electric_mirrors = Boolean()
    first_owner = Boolean()
    centralized_locking = Boolean()
    airbag = Boolean()  
    abs_break = Boolean()
    catalitic = Boolean()
    alarm = Boolean()
    kilometers = Integer()
    confirmed = Boolean()
    is_new = Boolean()

    class Meta:
        index = settings.ELASTICSEARCH_PUBLICATIONS_INDEX

class Publication(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    source = models.CharField(max_length=200)
    chileautos_id = models.IntegerField(null=True, unique=True)
    brand = models.ForeignKey(Brand)
    model = models.TextField(blank=True)
    model_version = models.TextField(blank=True)
    plate_number = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(City, null=True)
    region = models.ForeignKey(Region, null=True)
    year = models.IntegerField(default=2000)
    publication_date = models.DateTimeField(auto_now=True)
    type_of_vehicle = models.CharField(max_length=200, blank=True)
    vehicle_body = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=200, blank=True)
    fuel = models.CharField(max_length=200, blank=True)
    engine = models.FloatField(null=True)
    doors = models.IntegerField(default=0)
    at_transmission = models.NullBooleanField()
    assisted_steering = models.NullBooleanField()
    air_conditioner = models.NullBooleanField()
    electric_mirrors = models.NullBooleanField()
    first_owner = models.NullBooleanField()
    centralized_locking = models.NullBooleanField()
    airbag = models.NullBooleanField()
    abs_break = models.NullBooleanField()
    catalitic = models.NullBooleanField()
    alarm = models.NullBooleanField()
    kilometers = models.IntegerField(null=True)
    confirmed = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    contact_name = models.CharField(max_length=200, blank=True)

    @staticmethod
    @app.task
    def retrieve_from_chileautos_and_save(publication_id):
        publication = Publication.retrieve_from_chileautos(publication_id)
        publication.save()
        return publication

    @staticmethod
    def retrieve_from_chileautos(publication_id):
        existent = Publication.objects.filter(chileautos_id=publication_id).exists()
        if existent:
            # If already exists it may have changed so I retrieve it anyway
            publication = Publication.objects.get(chileautos_id=publication_id)
        else:
            publication = Publication()
        publication_json = ChileautosScrapper.retrieve_publication(publication_id)
        for key, value in publication_json.iteritems():
            if key not in ['brand', 'city', 'region', 'contact_numbers']:
                publication.__setattr__(key, value)
        
        # # Get brand from db or save new brand
        if 'brand' in publication_json.keys():
            brand, created = Brand.objects.get_or_create(name=publication_json.get('brand'))
            brand.save()
            publication.brand = brand


        if 'city' in publication_json.keys():
            city, created = City.objects.get_or_create(name=publication_json.get('city'))
            city.save()
            publication.city = city

        publication.save()

        if 'images' in publication_json.keys():
            for image_url in publication_json.get('images'):
                response = requests.get(image_url)
                temp_image = NamedTemporaryFile(delete=True)
                temp_image.write(response.content)
                temp_image.flush()
                publication_image, created = PublicationImage.objects.get_or_create(source_url=image_url)
                if created:
                    filename_regex = re.compile('g_([\w.]+)')
                    file_name = filename_regex.search(image_url).group()
                    publication_image.image.save(file_name, File(temp_image), save=True)
                    get_thumbnail(publication_image.image, '72x72', crop='center')
                    publication_image.source_url = image_url
                    publication_image.publication = publication
                    publication_image.save()
            get_thumbnail(publication.publication_images.first().image, '130x130', crop='center')
            


        if 'contact_numbers' in publication_json.keys():
            for contact_number in publication_json.get('contact_numbers'):
                phone = PhoneNumber(publication=publication, number=contact_number.get('number'), phone_type=contact_number.get('phone_type'))
                phone.save()
        publication.save()

        return publication

    
    def save(self, *args, **kwargs):
        # TODO: I have to make this iterative instead of this. But not automagic, not all the terms are indexed
        publication_index = Publication_index()
        publication_index.title = self.title
        publication_index.description = self.description
        publication_index.price = self.price
        publication_index.source = self.source
        publication_index.chileautos_id = self.chileautos_id
        if self.brand:
            publication_index.brand = self.brand.name
        publication_index.model = self.model
        publication_index.model_version = self.model_version
        publication_index.plate_number = self.plate_number
        if self.city:
            publication_index.city = self.city.name
        if self.region:
            publication_index.region = self.region.name
        publication_index.year = self.year
        # publication_index.publication_date = self.publication_date
        publication_index.type_of_vehicle = self.type_of_vehicle
        publication_index.vehicle_body = self.vehicle_body
        publication_index.color = self.color
        publication_index.fuel = self.fuel
        publication_index.engine = self.engine
        publication_index.at_transmission = self.at_transmission
        publication_index.assisted_steering = self.assisted_steering
        publication_index.air_conditioner = self.air_conditioner
        publication_index.electric_mirrors = self.electric_mirrors
        publication_index.first_owner = self.first_owner
        publication_index.centralized_locking = self.centralized_locking
        publication_index.airbag = self.airbag
        publication_index.abs_break = self.abs_break
        publication_index.catalitic = self.catalitic
        publication_index.alarm = self.alarm
        publication_index.kilometers = self.kilometers
        publication_index.confirmed = self.confirmed
        publication_index.new = self.is_new
        super(Publication, self).save(*args, **kwargs)
        publication_index.id = self.id
        publication_index.save()


    CHARACTERISTICS = [
      { 'key': 'brand', 'label': 'Marca', 'type': 'brand'},
      { 'key': 'model', 'label': 'Modelo', 'type': 'string'},
      { 'key': 'model_version', 'label': 'Versión', 'type': 'string'},
      { 'key': 'type_of_vehicle', 'label': 'Tipo de vehículo', 'type': 'string'},
      { 'key': 'vehicle_body', 'label': 'Chasis', 'type': 'string'},
      { 'key': 'fuel', 'label': 'Tipo de combustible', 'type': 'string'},
      { 'key': 'at_transmission', 'label': 'Transmisión', 'type': 'custom_boolean', 'alternatives': {'True': 'Automática', 'False': 'Mecánica'}},
      { 'key': 'air_conditioner', 'label': 'Aire acondicionado', 'type': 'boolean'},
      { 'key': 'first_owner', 'label': 'Primer dueño', 'type': 'boolean'},
      { 'key': 'centralized_locking', 'label': 'Cierre centralizado', 'type': 'boolean'},
      { 'key': 'airbag', 'label': 'Airbag', 'type': 'boolean'},
      { 'key': 'abs_break', 'label': 'Frenos ABS', 'type': 'boolean'},
      { 'key': 'catalitic', 'label': 'Catalítico', 'type': 'boolean'},
      { 'key': 'alarm', 'label': 'Alarma', 'type': 'boolean'},
      { 'key': 'assisted_steering', 'label': 'Dirección asistida', 'type': 'boolean'},
    ]

    def usage(self):
        if self.is_new:
          return "Nuevo"
        if self.is_new == False:
          return "Usado"
        return ""

    def get_characteristics(self):

        for characteristic in self.CHARACTERISTICS:
            if characteristic.get('type') == 'boolean':
                if self.__dict__.get(characteristic.get('key')):
                    characteristic['value'] = "Si"
                elif self.__dict__.get(characteristic.get('key')) == False:
                    characteristic['value'] = "No"
                else:
                    characteristic['value'] = None
            if characteristic.get('type') == 'string':
                characteristic['value'] = self.__dict__[characteristic.get('key')]
            if characteristic.get('type') == 'custom_boolean':
                characteristic['value'] = characteristic.get('alternatives').get('True') if self.__dict__[characteristic.get('key')] else characteristic.get('alternatives').get('False')
            if characteristic.get('type') == 'integer':
                characteristic['value'] = self.__dict__[characteristic.get('key')]
            if characteristic.get('type') == 'brand':
                characteristic['value'] = self.brand.name
        return self.CHARACTERISTICS


    def source_url(self):
        if self.chileautos_id:
            return "http://www.chileautos.cl/auto.asp?codauto=%s" % self.chileautos_id
        return "#"

    def source_name(self):
        if self.chileautos_id:
            return "Chileautos"
        return "TodoAutos"

class PhoneNumber(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, related_name='contact_numbers')    
    number = models.CharField(max_length=30)
    phone_type = models.CharField(max_length=30)

class PublicationImage(models.Model):
    source_url = models.CharField(max_length=300, null=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, related_name='publication_images')
    image =  ImageField(upload_to='publications')