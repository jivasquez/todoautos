from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Publication


def index(request):
    return render(request, "index.html")


def results(request):
    results = Publication.objects.all()
    return render(request, "results.html", {'publications':results})

def publication(request, publication_id):
    publication = Publication.objects.get(id=publication_id)
    return render(request, "publication.html", {'publication':publication})