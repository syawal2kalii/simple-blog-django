from django.shortcuts import render
from django.http import HttpResponse


def blogs(request):
    print("a")
    # return HttpResponse("test")
    context = {
        "title": "Blogs",

    }
    return render(request, 'blogsHome/index.html', context)
# Create your views here.
