from django.shortcuts import render
from django.http import HttpResponse


def blogs(request):
    print("a")
    # return HttpResponse("test")
    return render(request, 'blogsHome/index.html')
# Create your views here.
