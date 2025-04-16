from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blogg(request):
    print("blogg")
    return HttpResponse("blog do app")
