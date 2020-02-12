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


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")     # получение значения поля age
        comment = request.POST.get("comment")
        email = request.POST.get("email")
        return HttpResponse("<h2>Hello, {0}! age: {1}, email: {2}, comment: {3}</h2>".format(name,age,email,comment))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})