from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from main_app.models import Publication

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


def index(request):
    return render(request, "index.html")


def search(request):
    client = Elasticsearch()
    query = Q("multi_match", query=request.GET.get('q'), fields=['title', 'description', 'brand', 'type_of_vehicle', 'vehicle_body'])
    s = Search(using=client, index=settings.ELASTICSEARCH_PUBLICATIONS_INDEX).query(query)

    s.aggs.bucket('brands', 'terms', field='brand')
    s.aggs.bucket('regions', 'terms', field='region')
    s.aggs.bucket('cities', 'terms', field='city')
    s.aggs.bucket('years', 'terms', field='year')

    response = s.execute()
    result_ids = map(lambda x: x._meta.id, response)
    
    results = Publication.objects.filter(id__in=result_ids)
    
    return render(request, "results.html", {'publications':results, 'filters': response.aggregations})


def publication(request, publication_id):
    publication = Publication.objects.get(id=publication_id)
    return render(request, "publication.html", {'publication':publication, 'characteristics': publication.get_characteristics()})