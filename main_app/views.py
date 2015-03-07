from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Auto


def index(request):
    return render(request, "index.html")


def results(request):
    results = Auto.objects.all()
    return render(request, "results.html", {'autos':results})

