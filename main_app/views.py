from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Publication

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


def index(request):
    return render(request, "index.html")


def results(request):
    client = Elasticsearch()

    s = Search(using=client, index="publications").query("match", brand="toyota")
    response = s.execute()
    for hit in response:
        print(hit, hit.title)
    results = Publication.objects.all()
    return render(request, "results.html", {'publications':results})

def publication(request, publication_id):
    publication = Publication.objects.get(id=publication_id)
    
    return render(request, "publication.html", {'publication':publication, 'characteristics': publication.get_characteristics()})