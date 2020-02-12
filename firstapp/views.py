from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Index")
#
#
# def about(request):
#     return HttpResponse("About")
#
#
# def contact(request):
#     return HttpResponseRedirect("/about")
#
#
# def details(request):
#     return HttpResponsePermanentRedirect("/")

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Persons


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