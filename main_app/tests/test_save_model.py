# -*- encoding: utf-8 -*-

from datetime import datetime

from django.test import TestCase
from django.conf import settings
from elasticsearch import Elasticsearch

from todoautosscraper.chileautos_scraper import ChileautosScrapper
from main_app.models import Publication, Brand, City, Region

class TestPublicationSaved(TestCase):
    def setUp(self):
        brand = Brand(name="Nissan")
        brand.save()
        region = Region(name="RM")
        region.save()
        city = City(name="Santiago", region=region)
        city.save()
        publication = Publication()
        publication.title = "Publication title"
        publication.description = "Descripción de la publicacion"
        publication.price = 6300000
        publication.brand = brand
        publication.city = city
        publication.region = region
        publication.publication_date = datetime.now()
        publication.type_of_vehicle = "Camioneta"
        publication.vehicle_body = "Doble cabina"
        publication.fuel = "Petroleo"
        publication.at_transmission = True
        publication.air_conditioner = True
        publication.first_owner = True
        publication.centralized_locking = True
        publication.airbag = True
        publication.abs_break = True
        publication.kilometers = 60000
        publication.confirmed = True
        publication.save()

    def tearDown(self):
      es = Elasticsearch()
      es.indices.delete(settings.ELASTICSEARCH_PUBLICATIONS_INDEX, ignore=[400, 404])

    def test_check_db_store(self):
        """Check if things are stored on DB"""
        publications = Publication.objects.all()
        self.assertEqual(len(publications), 1)
        self.assertEqual(publications[0].brand.name, "Nissan")