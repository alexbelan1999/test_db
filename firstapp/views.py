from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .forms import Cylinder, Paral

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Persons
import math


# получение данных из бд
def index(request):
    people = Persons.objects.all()
    return render(request, "index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Persons()
        person.name = request.POST.get("name")
        person.addtime = request.POST.get("addtime")
        person.save()
    return HttpResponseRedirect("/")


def edit(request, id):
    try:
        person = Persons.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.addtime = request.POST.get("addtime")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Persons.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Persons.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Persons.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def cylinder(request):
    if request.method == "POST":
        form = Paral(request.POST)

        r = float(request.POST.get("r"))
        h = float(request.POST.get("h"))
        V = math.pi * r * r * h
        S = 2 * math.pi * r * (r + h)
        # return HttpResponse("<h2>Объем {0}, площадь поверхности {1}</h2>".format(V1,S1))
        return render(request, "cylinder.html", {"form": form, "square": S, "volume": V})

    else:
        form = Cylinder()
        return render(request, "cylinder.html", {"form": form})


def paral(request):
    if request.method == "POST":
        form = Paral(request.POST)

        a = float(request.POST.get("a"))
        b = float(request.POST.get("b"))
        c = float(request.POST.get("c"))
        V = a * b * c
        S = 2 * (a * b + b * c + a * c)
        # return HttpResponse("<h2>Объем {0}, площадь поверхности {1}</h2>".format(V1,S1))
        return render(request, "paral.html", {"form": form, "square": S, "volume": V})

    else:
        form = Paral()
        return render(request, "paral.html", {"form": form})
