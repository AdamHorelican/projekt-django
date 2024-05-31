from django.shortcuts import render, HttpResponse
from . models import *

def vypis_konzultantov(request):
    titul = Trieda.objects.all().order_by("nazov")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    studenti = Student.objects.all().order_by("priezvisko")
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"triedy":triedy, "ucitelia":ucitelia, "studenti":studenti, "kruzky":kruzky})
    

def vypis_studentov(request):
    studenti = Student.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"studenti":studenti})
