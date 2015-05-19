# -*- encoding: utf-8 -*-

from datetime import datetime

from django.test import TestCase
from django.conf import settings
from elasticsearch import Elasticsearch

from todoautosscraper.chileautos_scraper import ChileautosScrapper
from main_app.models import Publication, Brand, City, Region


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


        # publication = Publication.retrieve_from_chileautos(4522651)
        # self.assertEquals(publication.brand.name, 'Audi')
        # self.assertEquals(publication.chileautos_id, 4522651)
        # self.assertEquals(publication.city.name, "Santiago")
        # self.assertEquals(publication.plate_number, "WV2488")
        # self.assertEquals(publication.contact_numbers.all()[0].number, "99054960")
        # self.assertEquals(publication.contact_numbers.all()[0].phone_type, "mobile")

        publication2 = Publication.retrieve_from_chileautos(4552794)
        self.assertEquals(publication2.contact_numbers.all()[0].number, "42697585")
        self.assertEquals(publication2.contact_numbers.all()[1].number, "225261936")