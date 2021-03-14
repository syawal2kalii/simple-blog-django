from django.shortcuts import render
from django.http import HttpResponse


def blogs(request):
    print("a")
    return HttpResponse("test")
# Create your views here.
