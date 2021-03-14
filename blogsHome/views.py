from django.shortcuts import render
from django.http import HttpResponse


def blogs(request):
    print("a")
    # return HttpResponse("test")
    return render(request, "index1.html")
# Create your views here.
