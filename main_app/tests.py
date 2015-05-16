# -*- encoding: utf-8 -*-

from datetime import datetime

from django.test import TestCase
from django.conf import settings
from elasticsearch import Elasticsearch

from todoautosscraper.chileautos_scraper import ChileautosScrapper
from main_app.models import Publication, Brand, City, Region

class AnimalTestCase(TestCase):
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
        # self.assertEqual(brand.name, "Nissan")




class TestPublicationRetrieval(TestCase):
  

    def test_retrieve_publication(self):

        # This is just a handy reference
        # expected_json = {
        #   "brand": u"Audi",
        #   "model": u"A4",
        #   "model_version":  u"2.0 multitronic dies",
        #   "year":  2007,
        #   "type_of_vehicle": u"Automóvil",
        #   "vehicle_body": u"Sedán",
        #   "color":  u"gris",
        #   "kilometers":  100000,
        #   "engine" :  2000,
        #   "at_transmission":  True,
        #   "assisted_steering":  True,
        #   "air_conditioner": True,
        #   "electric_mirrors": True,
        #   "abs_break": True,
        #   "airbag": True,
        #   "centralized_locking": True,
        #   "catalitic": True,
        #   "fuel": u"Diesel (Petroleo)",
        #   "doors": 4,
        #   "alarm": True,
        #   "source": "chileautos"
        #   }


        publication = Publication.retrieve_from_chileautos(4553766)
        self.assertEquals(publication.brand.name, 'Audi')
        self.assertEquals(publication.chileautos_id, 4522651)
        self.assertEquals(publication.city.name, "Santiago")
        self.assertEquals(publication.plate_number, "WV2488")
        self.assertEquals(publication.contact_numbers.all()[0].number, "99054960")
        self.assertEquals(publication.contact_numbers.all()[0].phone_type, "mobile")
